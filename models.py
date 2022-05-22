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