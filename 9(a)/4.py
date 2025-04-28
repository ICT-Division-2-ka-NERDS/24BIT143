def isp(i):
    if type(i) == str and i == i[::-1]:
        return True
    else:
        return False

lst = ['madam','Python',"malayalam",12321]
t = list(filter(isp, lst))
print(t)
