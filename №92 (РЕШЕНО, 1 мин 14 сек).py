def t(x):
    y = 1
    count = 0
    while y < x + 1:
        a = y
        b = 0
        while b != 1:
            if b == 89:
                count += 1
                break
            if b != 0:
                a = b
                b = 0
            while a > 0:
                b += (a % 10) ** 2
                a //= 10
        y += 1
    print(count)

# вариант доработки
'''
def t(x):
    y = 1
    count = 0
    c1 = {1}
    c89 = {2, 89}
    while y < x + 1:
        a = y
        b = 0
        c = []
        g = 0
        while b != 1:
            if b != 0:
                a = b
                b = 0
            while a > 0:
                b += (a % 10) ** 2
                c.append((a % 10) ** 2)
                a //= 10
            if b in c1:
                break
            if b in c89:
                count += 1
                g = 1
                break
        c = set(c)
        if g == 0:
            c1 = c1.union(c)
        else:
            c89 = c89.union(c)
        y += 1
    print(count)
'''