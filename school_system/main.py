from student import Student
from lecturer import Lecturer

people = [
    Student("Ifeyemi", "200 Level"),
    Lecturer("Dr. Ade", "COS 201")
]

for person in people:
    print(person.get_role())
    print(person.get_info())
    print("-----")
