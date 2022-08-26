# функция проверки на истинность деления на каждое число в диапазоне
# n - проверяемое число, c - наибольший делитель в проверяемом диапазоне
def divisor_in_diap(n, c):
    while c > 0:
        if n % c == 0:
            c -= 1
        else:
            return False
    return True


# функция находит первое (т.е. наименьшее) число, которое делится нацело на все числа
# в диапазоне от 1 до y
def smallest_divisible(y):
    m = y
    while divisor_in_diap(m, y) is False:
        m += y
    return m

#  решил сам
