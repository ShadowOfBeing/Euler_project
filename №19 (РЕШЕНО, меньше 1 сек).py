day_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# стартовое значение первого дня недели
start = 0

# x - кладём в функцию день недели на 1 января текущего года и она возвращает день недели на
# 1 января следующего года, день недели задаём числом (от 1 до 7). y - год в формате XXXX.
def next_year(x, y):
    global start
    days_list = [[], [], [], [], [], [], [], [], [], [], [], []]
    # если год с двумя нулями в конце, тогда смотрим, делится ли он на 400 (високосный ли он)
    if y % 100 == 0:
        if y % 400 == 0:
            month1 = [x for x in month]; month1.pop(1); month1.insert(1, 29)
        else:
            month1 = [x for x in month]
    elif y % 4 == 0:
        month1 = [x for x in month]; month1.pop(1); month1.insert(1, 29)
    else:
        month1 = [x for x in month]
    s = x
    for i in range(len(month1)):
        for t in range(month1[i]):
            days_list[i].append(day_of_week[s])
            if s < 6:
                s += 1
            else:
                s = 0
    start = s
    return days_list


# x - стартовый год, y - конечный год
# год, месяц и число разделяются пробелами
def sunday_count(x, y):
    global start
    x1 = x
    count = 0
    # создаём список со вложенными списками в кол-ве равном количеству лет в заданном диапазоне
    for i in range(y - x + 1):
        year = next_year(start, x1)
        for u in year:
            if u[0] == 'Воскресенье':
                count += 1
        x1 += 1
    return count


next_year(start, 1900)
print(sunday_count(1901, 2000))
