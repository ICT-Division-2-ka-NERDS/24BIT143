names = [("John", "Mike"), "Emma", "Sophia", ("Tom", "Jake"), "Olivia"]
b = 0
g = 0

for name in names:
    if isinstance(name, tuple):
        b += 1
    else:
        g += 1

print("Boys:", b)
print("Girls:", g)
