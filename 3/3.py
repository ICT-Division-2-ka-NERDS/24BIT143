s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if s2 in s1:
    print(s2, "is found in", s1)
else:
    print(s2, "is not found in", s1)