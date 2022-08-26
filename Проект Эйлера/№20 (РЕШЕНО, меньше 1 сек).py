# функция разделяет число на цифры и суммирует их
def number_expansion_and_sum(n):
    s = n
    y = 0
    while s > 0:
        y += s % 10
        s //= 10
    return y


# функция нахождения факториала
def factorial(x):
    s = 1
    for i in range(1, x+1):
        s *= i
    return s


print(number_expansion_and_sum(factorial(100)))

# решил сам
