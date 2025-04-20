

marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))


if marks1 <= 39 or marks2 <= 39 or marks3 <= 39:
    result = "Fail"
else:
    result = "Pass"


total = marks1 + marks2 + marks3
average = total / 3


if marks1 == 0:
    grade1 = "F"
elif marks1 <= 39:
    grade1 = "F"
elif 40 <= marks1 <= 44:
    grade1 = "P"
elif 45 <= marks1 <= 49:
    grade1 = "C"
elif 50 <= marks1 <= 54:
    grade1 = "B"
elif 55 <= marks1 <= 59:
    grade1 = "B+"
elif 60 <= marks1 <= 69:
    grade1 = "A"
elif 70 <= marks1 <= 79:
    grade1 = "A+"
else:
    grade1 = "O"


if marks2 == 0:
    grade2 = "F"
elif marks2 <= 39:
    grade2 = "F"
elif 40 <= marks2 <= 44:
    grade2 = "P"
elif 45 <= marks2 <= 49:
    grade2 = "C"
elif 50 <= marks2 <= 54:
    grade2 = "B"
elif 55 <= marks2 <= 59:
    grade2 = "B+"
elif 60 <= marks2 <= 69:
    grade2 = "A"
elif 70 <= marks2 <= 79:
    grade2 = "A+"
else:
    grade2 = "O"

if marks3 == 0:
    grade3 = "F"
elif marks3 <= 39:
    grade3 = "F"
elif 40 <= marks3 <= 44:
    grade3 = "P"
elif 45 <= marks3 <= 49:
    grade3 = "C"
elif 50 <= marks3 <= 54:
    grade3 = "B"
elif 55 <= marks3 <= 59:
    grade3 = "B+"
elif 60 <= marks3 <= 69:
    grade3 = "A"
elif 70 <= marks3 <= 79:
    grade3 = "A+"
else:
    grade3 = "O"


print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Result: {result}")
print(f"Subject 1 Grade: {grade1}")
print(f"Subject 2 Grade: {grade2}")
print(f"Subject 3 Grade: {grade3}")
