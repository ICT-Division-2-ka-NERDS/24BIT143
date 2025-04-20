import random

odd = []
for i in range(5):
    odd.append(random.randrange(1, 100, 2))

even = []
for i in range(4):
    even.append(random.randrange(2, 101, 2))

odd[2] = even
flat = []
for i in odd:
    if type(i) == list:
        for j in i:
            flat.append(j)
    else:
        flat.append(i)

flat.sort()
print(flat)
