import random

nums = []
for i in range(50):
    nums.append(random.randint(1, 30))

unique = []
for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)
