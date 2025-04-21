import random
l1 = []
for i in range(0,10):
    a = random.randrange(15,45)
    l1.append(a)
numbers = set(l1)

print("Nums:", numbers)

count_less_than_30 = sum(1 for num in numbers if num < 30)
print("Count of num <30:", count_less_than_30)

numbers = {num for num in numbers if num <= 35}
print("After deletion of num > 35:", numbers)
