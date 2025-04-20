num = input("Enter a number: ")
if num.startswith('-'):
    num = num[1:]


dig = len(num)
print("Number of digits:", dig)
