# функция разделяет число на цифры и суммирует их
def number_expansion_and_sum(n):
    s = n
    y = 0
    while s > 0:
        y += s % 10
        s //= 10
    return y


print(number_expansion_and_sum(2**1000))

# решил сам
