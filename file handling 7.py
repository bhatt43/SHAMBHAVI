import pickle

class Employee:
    def _init_(self, code, name, doj, salary):
        self.code = code
        self.name = name
        self.doj = doj
        self.salary = salary

    def _str_(self):
        return f"{self.code}, {self.name}, {self.doj}, {self.salary}"

emp = Employee(101, 'John Doe', '2023-01-01', 50000)

with open('employee.dat', 'wb') as file:
    pickle.dump(emp, file)

with open('employee.dat', 'rb') as file:
    loaded_emp = pickle.load(file)

print("Deserialized Employee:", loaded_emp)

