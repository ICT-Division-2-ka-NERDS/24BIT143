import random

nums = []
for i in range(30):
    nums.append(random.randint(-50, 50))

pos = []
neg = []

for num in nums:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

print("Positive numbers:", pos)
print("Negative numbers:", neg)
