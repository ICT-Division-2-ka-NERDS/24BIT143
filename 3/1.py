
str = input("Enter a string: ")

v = 0


for char in str:
    
    if char.lower() in 'aeiou':
        v += 1

print(f"Number of vowels in the string: {v}")
