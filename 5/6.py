fahrenheit = [32, 45, 64, 72, 98]
celsius = []

for f in fahrenheit:
    c = (f - 32) * 5/9
    celsius.append(c)

print(celsius)
