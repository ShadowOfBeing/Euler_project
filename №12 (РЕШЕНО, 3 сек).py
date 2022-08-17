# функция возвращает количество делителей числа n
def number_of_divisors2(n):
    t = 0
    for i in range(1, int((n ** (1 / 2)) // 1 + 1)):
        if n % i == 0:
            t += 2
    if n % ((n ** (1 / 2)) // 1) == 0:
        t -= 1
    return t


# функция возвращает первое треугольное число, имеющее не менее x делителей
def triangular_number(x):
    a = [1]
    b = 1
    while number_of_divisors2(a[-1]) < x:
        b += 1
        a.append(a[-1] + b)
    return a[-1]
