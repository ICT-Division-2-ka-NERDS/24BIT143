def rmv(s1, s2):
    if s2 in s1:
        s1 = s1.replace(s2, "")
    return s1

s1 = input("Enter main string: ")
s2 = input("Enter string to remove: ")

result = rmv(s1, s2)
print("Final string:", result)
