n = int(input("Enter a number: "))

prime = True
if n < 2:
    prime = False
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        prime = False
        break


divisors = 0
for i in range(1, n):
    if n % i == 0:
        divisors += i
perfect = divisors == n

digits = 0
temp = n
numdigits = len(str(n))
while temp > 0:
    digits += (temp % 10) ** numdigits
    temp //= 10
armstrong = digits == n


palindrome = str(n) == str(n)[::-1]


square = n * n
automorphic = str(square).endswith(str(n))

print("Prime:", prime)
print("Perfect:", perfect)
print("Armstrong:", armstrong)
print("Palindrome:", palindrome)
print("Automorphic:", automorphic)
