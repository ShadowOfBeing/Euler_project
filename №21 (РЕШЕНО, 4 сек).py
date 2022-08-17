# функция находит все делители числа и суммирует их
def sum_of_divisors(x):
    y = 0
    for i in range(1, x):
        if x % i == 0:
            y += i
    return y


# функция находит все дружественные числа в заданном диапазоне и суммирует их
def sum_of_friendly_numbers(n):
    x = []
    for i in range(n):
        if i == (sum_of_divisors(sum_of_divisors(i))) and sum_of_divisors(i) != i:
            x.append(i)
    return sum(x)


print(sum_of_friendly_numbers(10000))

# решил сам
