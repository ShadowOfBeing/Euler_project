digits = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]

# удаляем из списка дубликаты
digits1 = []
for i in digits:
    if i not in digits1:
        digits1.append(i)

# представляем все числа в виде списков из трёх цифр
digits2 = []
for i in digits1:
    list1 = []
    while i > 0:
        list1.append(i % 10)
        i //= 10
    list1.reverse()
    digits2.append(list1)


# функция проверяет, удовлетворяет ли пароль всем трёхзначным кодам
# (необязательная функция для данной задачи)
def bruteforce(digit):
    # разбиваем число на цифры
    list2 = []
    while digit > 0:
        list2.append(digit % 10)
        digit //= 10
    list2.reverse()
    # проверяем, содержит ли число все коды из списка digits2
    for ii in digits2:
        list3 = list2.copy()
        for i1 in ii:
            if i1 in list3:
                del list3[:(list3.index(i1) + 1)]
            else:
                return False
    return True


# функция проверяет, содержит ли пароль трёхзначный код
# q - трёхзначный код, w - проверяемое число
def brut1(w1, q1):
    w = w1.copy()
    q = q1.copy()
    while len(q) > 0:
        if q[0] in w:
            del w[:(w.index(q[0]) + 1)]
            q.pop(0)
        else:
            return False
    return True


l = digits2.pop(0)
while len(digits2) > 0:
    for i in digits2:
        if brut1(l, i):
            k = digits2.index(i)
            digits2.pop(k)
            break
        for i1 in l:
            # если находимся с левого края
            if l.index(i1) == 0:
                if l[0] == i[1] and l[1] == i[2]:
                    l.insert(0, i[0])
                    digits2.remove(i)
            # если находимся с правого края
            elif l.index(i1) == len(l) - 1:
                if l[l.index(i1) - 1] == i[0] and i1 == i[1]:
                    l.append(i[2])
                    digits2.remove(i)
            # если находимся между краями
            if l[l.index(i1) - 1] == i[0] and i1 == i[2]:
                l.insert(l.index(i1), i[1])
                digits2.remove(i)
print(l)

# спорное решение, так как решение правильное именно для данного примера и лишь при
# условии, что в строке l = digits2.pop(0) будет использоваться именно элемент с
# индексом 0, остальные элементы не подходят
# тем не менее пароль найден верный
