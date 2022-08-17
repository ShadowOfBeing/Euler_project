a = 1
b = 2
c = 997
while a**2 + b**2 != c**2:
    if b < c:
        b += 1
        c = 1000 - (a + b)
    else:
        a += 1
        b = a + 1
        c = 1000 - (a + b)
print(a*b*c)

#  решил сам
