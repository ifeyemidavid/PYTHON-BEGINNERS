from person import Person

class Lecturer(Person):

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_role(self):
        return "Lecturer"

    def get_info(self):
        return f"Name: {self.name}, Course: {self.course}"
