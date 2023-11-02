
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.email = first + "." + last + "@Jmail.com"
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remv_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"> {emp.fullname()} <\n")


dev_1 = Developer("Corey", "Schafer", 58000, "Python")
dev_2 = Developer("Jack", "Booker", 67000, "Java")

mgr_1 = Manager("David", "Sarif", 100000, [dev_1])

print(issubclass(Developer, Manager))