def diagonal_sum(x):
    a = []
    b = [1]
    i = 1
    y, k = 0, 0
    while len(a) < x * x:
        a.append(i)
        i += 1
    while len(b) < x * 2 - 1:
        j = y + 1
        while j < 4 * (1 + y) + 1:
            b.append(a[k + 2 * j])
            j += 1 + y
        y += 1
        k = a.index(b[-1])
    print(sum(b))

# решил сам
