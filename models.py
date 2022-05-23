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
        self.begin_date = begin_date
        self.end_date = end_date
        self.description = description

    def __str__(self):
        return f'{self.id}, {self.begin_date}, {self.end_date}, {self.charge}, {self.description}'