class Employee:
    def __init__(self, employee_id, charge, name, email):
        self.id = employee_id
        self.charge = charge
        self.name = name
        self.email = email
        

class Charge:
    def __init__(self, charge_id, charge_name):
        self.charge_id = charge_id
        self.charge_name = charge_name
