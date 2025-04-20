x1 = float(input("Enter center x: "))
y1 = float(input("Enter center y: "))
r = float(input("Enter radius of the circle: "))
x2 = float(input("Enter point x: "))
y2 = float(input("Enter point y: "))


distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
if distance_squared < r ** 2:
    print("The point lies inside the circle.")
elif distance_squared == r ** 2:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")
