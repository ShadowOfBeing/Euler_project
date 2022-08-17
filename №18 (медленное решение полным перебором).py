import linecache
from itertools import product
'''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
x, x1, f = [], [], []
for i in range(4, 12):
    x.append([int(k) for k in linecache.getline('№18 (медленное решение полным перебором).py', i).split()])
    x1.append([int(k) for k in linecache.getline('№18 (медленное решение полным перебором).py', i).split()])


# функция заменяет каждый элемент его индексом во внутреннем списке
def index_of_list(list1):
    for k in range(len(list1)):
        for i in range(len(list1[k])):
            list1[k][i] = i
    return list1


x1 = index_of_list(x1)

# создаём все возможные комбинации элементов каждого списка с исходными элементами
s1 = list(product(*x))

# создаём все возможные комбинации элементов каждого списка с индексами
s2 = list(product(*x1))


# находим номера подходящих комбинаций и возвращаем их списком
def numbers_of_matching_combinations(s):
    q, w = [], []
    for k in s:
        for j in range(len(k) - 1):
            if 1 >= k[j] - k[j + 1] >= -1:
                w.append(k[j])
            else:
                break
            if j == len(k) - 2:
                w.append(k[-1])
        if len(w) == len(s[0]):
            q.append(s.index(k))
        w = []
    return q


value = numbers_of_matching_combinations(s2)

for i in value:
    f.append(sum(s1[i]))

print(max(f))
