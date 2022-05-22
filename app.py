# Imports para el desarrollo de la app
from flask import Flask, redirect, render_template, request, url_for
from models import Charge, Employee
import dbfunctions as dbf
# Entry point
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


# Vista en la cual se ven todos los empleados
# A partir de esta vista se puede acceder a create, update y delete
@app.route('/empleados')
def empleados():
    employee_list = []
    query = dbf.read(
        """SELECT idEmpleado, nombre, c.descripcion, correo FROM empleados e inner join cargos c on e.idCargo = c.idCargo ORDER BY nombre"""
    )
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
        dbf.create(
            f"""INSERT INTO empleados (idCargo, nombre, correo) VALUES({new_employee.charge}, "{new_employee.name}", "{new_employee.email}")"""
        )
        return redirect(url_for('empleados'))


@app.route('/actualizacionempleado', methods=['POST'])
def actualizacionempleado():
    updt_employee = Employee(int(request.form['idEmpleado']),
                             request.form['nombre'],
                             int(request.form['cargo']),
                             request.form['correo'])
    dbf.update(
        f"""UPDATE empleados SET nombre = '{updt_employee.name}', idCargo = {updt_employee.charge}, correo = '{updt_employee.email}' WHERE idEmpleado = {updt_employee.id}"""
    )
    return redirect(url_for('empleados'))


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


@app.route('/eliminarempleado', methods=['POST'])
def eliminarempleado():
    dbf.delete(
        f"""DELETE FROM empleados WHERE idEmpleado = {request.form['idEmpleado']}"""
    )
    return redirect(url_for('empleados'))
