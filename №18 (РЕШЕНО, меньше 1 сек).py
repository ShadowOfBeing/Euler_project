import linecache
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
x, x1, s = [], [], []

for i in range(3, 18):
    x.append([int(k) for k in linecache.getline('№18 (РЕШЕНО, меньше 1 сек).py', i).split()])
    x1.append([int(k) for k in linecache.getline('№18 (РЕШЕНО, меньше 1 сек).py', i).split()])


# функция заменяет каждый элемент его индексом во внутреннем списке
def index_of_list(list1):
    for k in range(len(list1)):
        for i in range(len(list1[k])):
            list1[k][i] = i
    return list1


x1 = index_of_list(x1)


def func2(ii2, ii1, y):
    if 0 <= ii2 - ii1 <= 1:
        return x1[y]
    else:
        return []


for i0 in x1[0]:
    for i1 in x1[1]:
        for i2 in x1[2]:
            for i3 in func2(i2, i1, 3):
                for i4 in func2(i3, i2, 4):
                    for i5 in func2(i4, i3, 5):
                        for i6 in func2(i5, i4, 6):
                            for i7 in func2(i6, i5, 7):
                                for i8 in func2(i7, i6, 8):
                                    for i9 in func2(i8, i7, 9):
                                        for i10 in func2(i9, i8, 10):
                                            for i11 in func2(i10, i9, 11):
                                                for i12 in func2(i11, i10, 12):
                                                    for i13 in func2(i12, i11, 13):
                                                        for i14 in x1[14]:
                                                            if 0 <= i14 - i13 <= 1:
                                                                s.append([x[0][i0], x[1][i1], x[2][i2], x[3][i3],
                                                                          x[4][i4], x[5][i5], x[6][i6], x[7][i7],
                                                                          x[8][i8], x[9][i9], x[10][i10], x[11][i11],
                                                                          x[12][i12], x[13][i13], x[14][i14]])

s = max([sum(x) for x in s])
print(s)

# решил сам
