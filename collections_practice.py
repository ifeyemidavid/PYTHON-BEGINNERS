# 1. Lists
students = ["Ifeyemi", "Akin", "Ngozi"]
students.append("Tunde")  # Add a student named Tunde
print("List of students:", students)

# 2. Tuples
grades = (85, 90, 78)
print("Grades tuple:", grades)

# 3. Sets
subjects = {"Math", "English", "Physics"}
subjects.add("Biology")
print("Subjects set:", subjects)

# 4. Dictionaries
student_scores = {"Ifeyemi": 85, "Akin": 90}
student_scores["Ngozi"] = 78
print("Student scores:", student_scores)

# using math module
import math
print("square root of 16 is:", math.sqrt(16))

# using random module
import random
print("Random student from the list:", random.choice(students))

# using datetime module
from datetime import datetime
print("Time:", datetime.now())
