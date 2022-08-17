# создаём все возможные перестановки
a = [0, 1, 2]
b = ['0', '1', '2']


# def combinations(x, y):
#     all_comb_arr = []
#     result = ''.join(b)
#     counter = 1
#     while counter < 3:
#
#
#     return result

'''
0123
0132
0213
0231
0312
0321
1023
1032
1203
1230
1302
1320
2013
2031
2103
2130
2301
2310
3012
3021
3102
3120
3201
3210
'''

# print(combinations(a, b))

def aa(x):
    counter = 0
    number = 0
    while counter < 4:
        # разбиваем число на строковые символы и помещаем в массив
        tmp_arr = [s for s in str(number)]
        # если не хватает 1 символа, то добавляем 0
        if len(x) - len(tmp_arr) == 1:
            tmp_arr.insert(0, "0")
        tmp = tmp_arr
        # удаляем все дубликаты
        tmp_arr = list(set(tmp_arr))
        if len(tmp_arr) == len(x):
            for i in tmp_arr:
                if i not in x:
                    break
                if i == tmp_arr[-1]:
                    print(tmp)
                    counter += 1
        number += 1

aa(b)
