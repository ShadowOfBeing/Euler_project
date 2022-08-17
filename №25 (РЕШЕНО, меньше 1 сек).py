def fibonacci_number_of_length_x(x):
    a = [1, 1]
    i = 0
    while len(str(a[-1])) < x:
        s = a[i] + a[i + 1]
        a.append(s)
        i += 1
    print(len(a))

# решил сам
