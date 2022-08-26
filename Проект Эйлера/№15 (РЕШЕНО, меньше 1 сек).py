# функция находит числа строки на основе предыдущей строки
def next_string(x):
    s = [1]
    for i in range(1, len(x)):
        s.append(x[i] + s[i - 1])
    return s


def find_sum_of_paths(x):
    a = [i for i in range(1, x + 1)]
    b = [i for i in a]
    for i in range(x - 2):
        c = next_string(b)
        a += c
        b = c
    print(sum(a) + x + 1)

# решил с подсказкой
