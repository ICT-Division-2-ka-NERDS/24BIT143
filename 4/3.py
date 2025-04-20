s = input("Enter a string: ")
alpha_count = 0
digit_count = 0

for c in s:
    if c.isalpha():
        alpha_count += 1
    elif c.isdigit():
        digit_count += 1


print("Alphabets:", alpha_count)
print("Digits:", digit_count)
