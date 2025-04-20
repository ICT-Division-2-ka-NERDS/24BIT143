import random

nums = []
for i in range(20):
    nums.append(random.randint(1, 100))

n = int(input("Enter a number: "))
positions = []
for i in range(len(nums)):
    if nums[i] == n:
        positions.append(i)

print("Positions:", positions)
