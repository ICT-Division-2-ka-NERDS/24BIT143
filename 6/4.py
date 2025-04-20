

def get_price(item):
    return item[1]

food = [("Pizza", 100), ("Burger", 80), ("Pasta", 60), ("Salad", 20)]

food.sort(key=get_price, reverse=True)

print(food)