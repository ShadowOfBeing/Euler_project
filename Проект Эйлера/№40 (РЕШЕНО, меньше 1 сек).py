# создаёт список из чисел последовательности Чамперноуна
def champernowne_constant_list(y):
    b = 9
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(a) < y:
        b += 1
        c = b
        c1 = []
        while c > 9:
            c1.append(c % 10)
            c //= 10
        c1.append(c)
        c1.reverse()
        a += c1
    return a


# аналогично функции выше, но возвращает произведение элементов списка по индексам i - 1 для
# диапазона от y до 1 включительно с шагом //10
def champernowne_constant_list1(y):
    b = 9
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(a) < y:
        b += 1
        c = b
        c1 = []
        while c > 9:
            c1.append(c % 10)
            c //= 10
        c1.append(c)
        c1.reverse()
        a += c1
    s2 = [y]
    s3 = y
    s = 1
    while s2[-1] > 1:
        s3 //= 10
        s2.append(s3)
    for i in s2:
        s *= a[i - 1]
    return s


# решил сам
