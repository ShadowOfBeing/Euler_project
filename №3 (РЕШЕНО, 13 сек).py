# функция поиска простых чисел
def simple_digit(n):
    if n == 2:
        return True
    for i in range(2, int(n ** (1 / 2)) // 1 + 1):
        if n % i == 0:
            return False
    return True


# функция поиска наибольшего простого делителя
def greatest_simple_divisor(x):
    a = 0
    for b in range(2, (x // 2) + 1):
        if x % b == 0:
            if simple_digit(x // b):
                a = x // b
                return a
    return "simple divisor not found"
# решил сам
