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


#Vista en la cual se ven todos los empleados, falta implementar que el cargo sea asociado con el nombre
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
        return redirect(url_for('nuevoempleado'))


@app.route('/actualizarempleado', methods=['GET', 'POST'])
def actualizarempleado():
    if request.method == 'GET':
        charges_list = []
        query = dbf.read("""SELECT * FROM cargos""")
        for item in query:
            new_charge = Charge(item[0], item[1])
            charges_list.append(new_charge)
        id_list = dbf.read(
            """SELECT idEmpleado, nombre, c.descripcion FROM empleados e inner join cargos c on e.idCargo = c.idCargo ORDER BY nombre"""
        )
        # id_list = dbf.read("""SELECT idEmpleado FROM empleados""")
        return render_template('actualizarempleado.html',
                               charges_list=charges_list,
                               id_list=id_list)
    elif request.method == 'POST':
        updt_employee = Employee(int(request.form['idEmpleado']),
                                 request.form['nombre'],
                                 int(request.form['cargo']),
                                 request.form['correo'])
        dbf.update(
            f"""UPDATE empleados SET nombre = '{updt_employee.name}', idCargo = {updt_employee.charge}, correo = '{updt_employee.email}' WHERE idEmpleado = {updt_employee.id}"""
        )
        return redirect(url_for('actualizarempleado'))
