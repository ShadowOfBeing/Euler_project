# функция проверяет является ли число простым
def simple_digit(n):
    if n == 2:
        return True
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


# функция создаёт список простых чисел длиной x и возвращает последний элемент списка
def c(x):
    x = 10001
    b = []
    k = 2
    while len(b) < x:
        if simple_digit(k):
            b.append(k)
        k += 1
    return b[-1]


# решил сам
