# создаём список простых чисел меньше 2000000 с помощью решета Эратосфена
def list_of_simple_digit_in_diap(n):
    a, b = [], []
    n = 2000000
    for i in range(n):
        a.append(i)
    a[1] = 0
    i = 2
    while i < n:
        if a[i] != 0:
            j = i + i
            while j < n:
                a[j] = 0
                j = j + i
        i += 1
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b


print(sum(list_of_simple_digit_in_diap(2000000)))

# решил сам
