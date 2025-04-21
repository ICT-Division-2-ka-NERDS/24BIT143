def count_vowels(text):
    if text == "":
        return 0
    if text[0].lower() in "aeiou":
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])

x = input("Enter a string: ")
print(count_vowels(x))
