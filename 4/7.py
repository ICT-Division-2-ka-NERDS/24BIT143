def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print("nCr:", nCr(n, r))
print("nPr:", nPr(n, r))
