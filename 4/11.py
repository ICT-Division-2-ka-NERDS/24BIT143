def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def sin_x(x, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        power = 2 * n + 1
        result += sign * (x ** power) / factorial(power)
    return result

x = float(input("Enter x in radians: "))
print("sin(x):", sin_x(x))
