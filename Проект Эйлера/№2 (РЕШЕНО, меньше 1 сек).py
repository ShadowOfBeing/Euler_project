def sum_of_even_fibonacci_numbers(x):
    a = [1, 2]
    i, j = 0, 0
    while a[-1] < x:
        s = a[i] + a[i + 1]
        a.append(s)
        i += 1
        if s % 2 == 0:
            j += s
    print(j)

# решил сам
