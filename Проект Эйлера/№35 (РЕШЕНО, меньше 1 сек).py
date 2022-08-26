# функция проверяет является ли число простым
def simple_digit(n):
    if n == 2:
        return True
    for i in range(2, int(n ** (1 / 2)) // 1 + 1):
        if n % i == 0:
            return False
    return True


# решето Эратосфена
def list_of_simple_digit_in_diap(n):
    a, b = [], []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b


# берёт последнюю цифру числа и вставляет в начало
def create_circular_number(x):
    a = 0
    b = x
    while b > 0:
        a += 1
        b //= 10
    b = x
    c = ((b % 10) * (10 ** (a - 1))) + (b // 10)
    return c


# создаёт список из всех круговых чисел
def create_all_circular_numbers(x):
    a = [x]
    b = create_circular_number(x)
    if b != a[0]:
        a.append(b)
    while create_circular_number(b) != x:
        b = create_circular_number(b)
        a.append(b)
    return a


# проверяет, являются ли все возможные круговые числа для x простыми
def checking_simple_circular_numbers(x):
    b = create_circular_number(x)
    if simple_digit(b):
        while create_circular_number(b) != x:
            if simple_digit(create_circular_number(b)):
                b = create_circular_number(b)
            else:
                return False
    else:
        return False
    return True


def all_simple_circular_numbers(u):
    h = []
    h1 = list_of_simple_digit_in_diap(u)
    for k in h1:
        if k in h:
            continue
        elif checking_simple_circular_numbers(k):
            for i in create_all_circular_numbers(k):
                h.append(i)
    print(len(h))

# решил сам
