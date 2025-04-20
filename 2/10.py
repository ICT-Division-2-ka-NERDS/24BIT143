l = float(input("Enter length of the rectangle: "))
b = float(input("Enter breadth of the rectangle: "))


a = l * b
p = 2 * (l + b)

if a> p:
    print("Area is greater than perimeter")
else:
    print("Area is not greater than perimeter")