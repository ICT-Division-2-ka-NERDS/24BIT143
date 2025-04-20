tuples = [(), ("Pizza", 12), (), ("Burger", 5), ("Pasta", 8)]

filtered = []
for i in tuples:
    if i:
        filtered.append(i)

print(filtered)
