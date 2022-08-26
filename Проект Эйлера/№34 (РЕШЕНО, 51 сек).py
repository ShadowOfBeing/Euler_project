# функция нахождения факториала
def factorial(x):
    s = 1
    for i in range(1, x+1):
        s *= i
    return s


# функция разделяет число на цифры и суммирует их факториалы
def number_expansion_and_sum(n):
    s = n
    y = 0
    while s > 0:
        y += factorial(s % 10)
        s //= 10
    return y


sum1 = 0
for i1 in range(3, 9999999):
    if number_expansion_and_sum(i1) == i1:
        sum1 += i1
        print(i1)
print(sum1)

# можно оптимизировать код для более быстрого выполнения, нужно сократить
# диапазон вычислений
