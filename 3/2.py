def low(s):
    r = ""
    for c in s:
        if 'A' <= c <= 'Z':
            r += chr(ord(c) + 32)
        else:
            r += c
    return r

def up(s):
    r = ""
    for c in s:
        if 'a' <= c <= 'z':
            r += chr(ord(c) - 32)
        else:
            r += c
    return r

def toggle(s):
    r = ""
    for c in s:
        if 'a' <= c <= 'z':
            r += chr(ord(c) - 32)
        elif 'A' <= c <= 'Z':
            r += chr(ord(c) + 32)
        else:
            r += c
    return r

str = input("Enter a string: ")
print(f"Lower case: {low(str)}")
print(f"Upper case: {up(str)}")
print(f"Toggled case: {toggle(str)}")
