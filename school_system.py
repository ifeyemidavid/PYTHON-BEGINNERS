from abc import ABC, abstractmethod

class person(ABC):

     @abstractmethod
     def get_role(self):
        pass

     @abstractmethod
     def get_info(self):
         pass

class Student(person):

    def __init__ (self, name, level):
        self.name = name
        self.level = level

    def get_role(self):
        return "Student"

    def get_info(self):
        return f"Name:{self.name}, Level:{self.level}"


class Lecturer(person):

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_role(self):
        return "Lecturer"

    def get_info(self):
        return f"Name:{self.name}, Course:{self.course}"

class Administrator (person):

    def __init__(self, name, office):
        self.name = name
        self.office = office

    def get_role(self):
        return "Administration"

    def get_info(self):
        return f"Name: {self.name}, Office: {self.office}"


people = [
    Student("ifeyemi", "200 Level"),
    Lecturer("DR. Ade", "COS 201"),
    Administrator("Mrs. Bello", "Registry")
]

for person in people:
    print(person.get_role())
    print(person.get_info())
    print("_____")





 