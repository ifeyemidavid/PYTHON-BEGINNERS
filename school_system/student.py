from person import Person

class Student(Person):

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_role(self):
        return "Student"
    
    def get_info(self):
        return f"Name: {self.name}, Level: {self.level}"

