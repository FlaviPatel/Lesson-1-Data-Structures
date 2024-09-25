students = {"name": "Riya", "roll" : "20", "age" : "13", "Subjects" : ["Maths, Science"]}

print(students)

print("Student name:", students["name"])
print("Student Roll No:", students["roll"])
print("Student age:", students.get("age"))

# Updating
students["age"] = 15
print(students)

# Adding
students["address"] = "House no. 23, colony: 2"
print(students)

students.clear()
print("Clearing the dictionary:", students)