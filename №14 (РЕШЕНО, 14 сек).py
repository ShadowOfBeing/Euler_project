# заранее высчитываем длину последовательностей Коллатца всех чисел от 1 до 50000
b1 = [1, 1]
for i in range(2, 50000 + 1):
    b = [i]
    y = i
    while b[-1] != 1:
        if y % 2 == 0:
            y //= 2
            b.append(y)
        else:
            y = y * 3 + 1
            b.append(y)
    b1.append(len(b))


# функция создаёт Сиракузскую последовательность для числа x
def syracuse_sequence(x):
    b = [x]
    y = x
    while b[-1] != 1:
        if b[-1] < 50001:
            return len(b) - 1 + b1[b[-1]]
        if y % 2 == 0:
            y //= 2
            b.append(y)
        else:
            y = y * 3 + 1
            b.append(y)
    return len(b)


# находим число с самой длинной последовательностью Коллатца
def longest_syracuse_sequence(t):
    u = 0
    u1 = 0
    for i in range(1, t):
        if syracuse_sequence(i) > u:
            u = syracuse_sequence(i)
            u1 = i
    return u1

print(longest_syracuse_sequence(1000000))

#  решил сам
