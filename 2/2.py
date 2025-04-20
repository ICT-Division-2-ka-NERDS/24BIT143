a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a >= b and a >= c:
    large = a
elif b >= a and b >= c:
    large = b
else:
    large = c


if a <= b and a <= c:
    small = a
elif b <= a and b <= c:
    small = b
else:
    small = c

print("Largest:", large)
print("Smallest:", small)
