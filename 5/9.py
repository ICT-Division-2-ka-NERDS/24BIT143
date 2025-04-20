l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
l3 = []

for num in l1:
    if num not in l2:
        l3.append(num)

print(l3)
