# функция поиска всех делителей числа
def dividers(number):
    div_arr = [1]
    for i in range(2, number):
        if number % i == 0:
            div_arr.append(i)
    return div_arr


# функция определения является ли число избыточным
def abundant(number):
    if sum(dividers(number)) > number:
        return True
    return False


# находим все избыточные числа от 12 до 28123
abundant_arr = [i for i in range(12, 28124) if abundant(i)]
sum_abundant = []
# находим все возможные суммы избыточных чисел
for i in abundant_arr:
    for k in abundant_arr[abundant_arr.index(i):]:
        if (i + k) >= 28124:
            break
        sum_abundant.append(i + k)

# создаём массив с последовательностью чисел от 1 до 28123
arr_numbers = [x for x in range(1, 28124)]

# вычитаем из всех чисел массива arr_numbers все найденные суммы избыточных чисел
print(sum(set(arr_numbers) - set(sum_abundant)))

# решил сам
