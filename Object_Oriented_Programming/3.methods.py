
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    
    # instance method
    # must create an object of the class before accessing it
    def getinfo(self):
        return self.name + " earns " + str(self.salary)

    
    # static method
    # can be used without creating an instance of the class but does not have access to any property of the class
    @staticmethod
    def employee_tax(salary, taxPercent):
        return salary * taxPercent

    @classmethod
    def get_employee_salary_and_info(cls, name, salary, taxPercent):
        return cls(name, salary).getinfo() + " with tax of " + str(cls.employee_tax(salary, taxPercent))


# calling an instance method
emp1 = Employee("Hussaini", 4000)
print(emp1.getinfo())


# calling a static method
emptax = Employee.employee_tax(4000, 0.01)
print(emptax)


# calling a classmethod
emp2 = Employee.get_employee_salary_and_info("Hussaini", 4000, 0.01)
print(emp2)
