class Employee:

    def __init__(self, employee_id, charge, name, email):
        self.id = employee_id
        self.charge = charge
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.id}, {self.charge}, {self.name}, {self.email}'


class Charge:

    def __init__(self, charge_id, charge_name):
        self.charge_id = charge_id
        self.charge_name = charge_name

    def __str__(self):
        return f'{self.charge_id}: {self.charge_name}'