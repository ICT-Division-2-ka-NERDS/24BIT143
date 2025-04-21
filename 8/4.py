names = {"arpit", "bob", "ananya", "bruce", "alice", "charlie"}

a = set()
b = set()

for name in names:
    if name.startswith('a'):
        a.add(name)
    elif name.startswith('b'):
        b.add(name)

print("Names starting with A:", a)
print("Names starting with B:", b)
