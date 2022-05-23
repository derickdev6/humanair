# Imports para el desarrollo de la app
from multiprocessing import Event
from flask import Flask, redirect, render_template, request, url_for
from models import Charge, Employee, mEvent, User, Task
import dbfunctions as dbf
# Entry point
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.form)
        login_user = User(request.form['username'], request.form['password'])
        if login_user.exists():
            print("Correct user")
            return redirect(url_for('home'))
        else:
            print("Incorrect User")
            return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


# Vista en la cual se ven todos los empleados
# A partir de esta vista se puede acceder a create, update y delete
@app.route('/empleados')
def empleados():
    employee_list = []
    query = dbf.read("""SELECT idEmpleado, nombre, c.descripcion, correo 
        FROM empleados e inner join cargos c on e.idCargo = c.idCargo 
        ORDER BY nombre""")
    for item in query:
        new_emp = Employee(item[0], item[1], item[2], item[3])
        employee_list.append(new_emp)

    return render_template('empleados.html', employee_list=employee_list)


# Esta ruta funciona como vista y como post
# Cuando es vista renderiza el formulario de nuevo empleado
# En el formulario el boton de crear manda un post a su misma ruta,
# donde se ejecuta un llamado a la funcion de create con los datos del formulario
@app.route('/nuevoempleado', methods=['GET', 'POST'])
def nuevoempleado():
    if request.method == 'GET':
        charges_list = []
        query = dbf.read("""SELECT * FROM cargos""")
        for item in query:
            new_charge = Charge(item[0], item[1])
            charges_list.append(new_charge)
        return render_template('nuevoempleado.html', charges_list=charges_list)
    elif request.method == 'POST':
        new_employee = Employee(0, request.form['nombre'],
                                int(request.form['cargo']),
                                request.form['correo'])
        # print(str(new_employee))
        dbf.create(f"""INSERT INTO empleados (idCargo, nombre, correo) 
            VALUES({new_employee.charge}, "{new_employee.name}", "{new_employee.email}")"""
                   )
        return redirect(url_for('empleados'))


# Ruta para la vista de actualizacion de empleado.
# Se usa desde el tool update de la lista de empleados.
# Muestra un template con los datos del empleado desde el cual se lanzo
@app.route('/actualizarempleado', methods=['POST'])
def actualizarempleado():
    charges_list = []
    query = dbf.read("""SELECT * FROM cargos""")
    for item in query:
        new_charge = Charge(item[0], item[1])
        charges_list.append(new_charge)
    emp_to_update = Employee(int(request.form['idEmpleado']),
                             request.form['nombre'], 1, request.form['correo'])
    return render_template('actualizarempleado.html',
                           charges_list=charges_list,
                           emp_to_update=emp_to_update)


# Ruta para la actualizacion de empleados.
# Unicamente se usa como post y es llamada desde el boton
# actualizar del template de actualizarempleado
@app.route('/actualizacionempleado', methods=['POST'])
def actualizacionempleado():
    updt_employee = Employee(int(request.form['idEmpleado']),
                             request.form['nombre'],
                             int(request.form['cargo']),
                             request.form['correo'])
    dbf.update(f"""UPDATE empleados SET 
        nombre = '{updt_employee.name}', 
        idCargo = {updt_employee.charge}, 
        correo = '{updt_employee.email}' 
        WHERE idEmpleado = {updt_employee.id}""")
    return redirect(url_for('empleados'))


# Eliminar empleado, se lanza desde el tool delete
# de la lista de empleados y elimina directamente al
# empleado desde el cual se lanzo
@app.route('/eliminarempleado', methods=['POST'])
def eliminarempleado():
    dbf.delete(
        f"""DELETE FROM empleados WHERE idEmpleado = {request.form['idEmpleado']}"""
    )
    return redirect(url_for('empleados'))


# Vista en la cual se ven todos los eventos
# A partir de esta vista se puede acceder a create
@app.route('/eventos')
def eventos():
    event_list = []
    query = dbf.read(
        """SELECT idEvento, fechaInicio, fechaFin, c.descripcion, e.descripcion 
            FROM eventos e inner join cargos c on e.idCargo = c.idCargo """)
    for item in query:
        # print(item)
        new_event = mEvent(item[0], item[1], item[2], item[3], item[4])
        # print(str(new_event))
        event_list.append(new_event)
    return render_template('eventos.html', event_list=event_list)


## Vista de creacion de un nuevo evento
@app.route('/nuevoevento', methods=['GET', 'POST'])
def nuevoevento():
    if request.method == 'GET':
        charges_list = []
        query = dbf.read("""SELECT * FROM cargos""")
        for item in query:
            new_charge = Charge(item[0], item[1])
            charges_list.append(new_charge)
        return render_template('nuevoevento.html', charges_list=charges_list)
    elif request.method == 'POST':
        new_event = mEvent(0, request.form['fecha_ini'],
                           request.form['fecha_fin'], request.form['cargo'],
                           request.form['descripcion'])
        print(str(new_event))
        dbf.create(
            f"""INSERT INTO eventos (idCargo , fechaInicio, fechaFin, descripcion) 
            VALUES({new_event.charge}, "{new_event.begin_date}", "{new_event.end_date}", "{new_event.description}")"""
        )
        return redirect(url_for('eventos'))


@app.route('/tareas')
def tareas():
    task_list = []
    query = dbf.read("""SELECT * FROM tareas """)
    for item in query:
        print(item)
        new_task = Task(item[0], item[1])
        print(str(new_task))
        task_list.append(new_task)
    return render_template('tareas.html', task_list=task_list)


## Vista de creacion de una nueva tarea
@app.route('/nuevatarea', methods=['POST'])
def nuevatarea():
    new_task = Task(0, request.form['nombre'])
    print(str(new_task))
    dbf.create(f"""INSERT INTO tareas (nombre) VALUES("{new_task.name}")""")
    return redirect(url_for('tareas'))


# Ruta para la vista de asignacion de empleado a una tarea.
# Se usa desde el tool asignar de la lista de tareas.
# Muestra un template con los datos de la tarea desde el cual se lanzo
@app.route('/asignarempleado', methods=['POST'])
def asignarempleado():
    employee_list = []
    query = dbf.read("""SELECT idEmpleado, nombre, c.descripcion, correo 
        FROM empleados e inner join cargos c on e.idCargo = c.idCargo 
        ORDER BY nombre""")
    for item in query:
        new_emp = Employee(item[0], item[1], item[2], item[3])
        employee_list.append(new_emp)

    assigned_list = []
    query = dbf.read(f"""SELECT e.idEmpleado, e.nombre 
        FROM tareasxempleado t inner join 
        empleados e on t.idEmpleado = e.idEmpleado 
        where t.idTarea = {int(request.form['idTarea'])}
        ORDER BY nombre""")
    for item in query:
        new_emp = Employee(item[0], item[1], 0, '')
        assigned_list.append(new_emp)

    task_to_assign = Task(int(request.form['idTarea']), request.form['nombre'])
    return render_template('asignarempleado.html',
                           task_to_assign=task_to_assign,
                           employee_list=employee_list,
                           assigned_list=assigned_list)


# Ruta para la asignacion de empleados.
# Unicamente se usa como post y es llamada desde el boton
# actualizar del template de asignarempleado
@app.route('/asignacionempleado', methods=['POST'])
def asignacionempleado():
    dbf.update(
        f"""INSERT INTO tareasxempleado (idTarea, idEmpleado) VALUES({request.form['idTarea']}, {request.form['idEmpleado']})"""
    )
    return redirect(url_for('tareas'))
