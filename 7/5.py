prices = {'apple': 10, 'banana': 5, 'cherry': 20}
quantity = {'apple': 3, 'banana': 2, 'cherry': 5}

totalbill = 0
for item in prices:
    totalbill += prices[item] * quantity.get(item, 0)

print(f"Total bill: {totalbill}")
