import dbfunctions as dbf


class Employee:

    def __init__(self, employee_id, name, charge, email):
        self.id = employee_id
        self.name = name
        self.charge = charge
        self.email = email

    def __str__(self):
        return f'{self.id}, {self.name}, {self.charge}, {self.email}'


class Charge:

    def __init__(self, charge_id, charge_name):
        self.id = charge_id
        self.name = charge_name

    def __str__(self):
        return f'{self.id}: {self.name}'


class mEvent:

    def __init__(self, event_id, begin_date, end_date, charge, description):
        self.id = event_id
        self.charge = charge
        self.begin_date = f'{begin_date[8:10]}/{begin_date[5:7]}/{begin_date[0:4]}'
        self.end_date = f'{end_date[8:10]}/{end_date[5:7]}/{end_date[0:4]}'
        self.description = description

    def __str__(self):
        return f'{self.id}, {self.begin_date}, {self.end_date}, {self.charge}, {self.description}'


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def exists(self):
        query = dbf.read(
            f"""SELECT * FROM users WHERE username = '{self.username}' AND password = '{self.password}'"""
        )
        if query:
            return True
        else:
            return False


class Task:

    def __init__(self, task_id, name):
        self.id = task_id
        self.name = name

    def __str__(self):
        return f'{self.id}: {self.name}'
