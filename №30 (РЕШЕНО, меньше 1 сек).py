# функция раскладывает число (n) на цифры, возводит их в нужную степень (c)
# и суммирует полученные цифры
def sum_of_degrees_of_digits(n, a):
    f = n
    e = 0
    while f > 0:
        e += (f % 10) ** a
        f //= 10
    return e


# тоже, что и функция выше, но ещё сравнивает (e) с (n) и возвращает True если они
# равны и False, если не равны
def sum_of_degrees_of_digits_true_false(n, a):
    f = n
    e = 0
    while f > 0:
        e += (f % 10) ** a
        f //= 10
    if e == n:
        return True
    else:
        return False


# функция находит в заданном диапазоне все подходящие числа и суммирует их
# первым действием функция вычисляет верхнюю планку необходимого диапазона
def the_sum_of_the_degrees_of_the_digits_of_the_correct_numbers(c):
    s, d = 9, 9
    q = 0
    while s ** c > d:
        d = d*10 + d
    while sum_of_degrees_of_digits(d, c) > d:
        d = d*10 + d
    for i in range(2, d):
        if sum_of_degrees_of_digits_true_false(i, c) is True:
            q += i
    print(q)


the_sum_of_the_degrees_of_the_digits_of_the_correct_numbers(5)
# решил сам
