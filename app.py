# Imports para el desarrollo de la app
from flask import Flask, redirect, render_template, url_for
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
    query = dbf.read("""SELECT * FROM empleados""")
    for item in query:
        new_emp = Employee(item[0], item[1], item[2], item[3])
        employee_list.append(new_emp)

    return render_template('empleados.html', employee_list=employee_list)
