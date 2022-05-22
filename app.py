# Imports para el desarrollo de la app
from flask import Flask, render_template
from models import Charge, Employee
import dbfunctions as dbf
# Entry point
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"
