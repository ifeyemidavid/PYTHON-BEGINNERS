from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass


class Developer(Employee):

    def get_role(self):
        return "Developer"

    def get_salary(self):
        return 250000


class Manager(Employee):

    def get_role(self):
        return "Manager"

    def get_salary(self):
        return 400000

    

employees = [Developer(), Manager()]

for emp in employees:
    print(emp.get_role())
    print(emp.get_salary())
    print("-----")