students = [(1, "John", 20), (2, "Emma", 22), (3, "Mike", 21)]
rollno = []
name = []
age = []

for student in students:
    rollno.append(student[0])
    name.append(student[1])
    age.append(student[2])

print("Roll No:", rollno)
print("Name:", name)
print("Age:", age)
