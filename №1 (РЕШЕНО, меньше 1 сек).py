def summ_3_5(n):
    a = 0
    for x in range(n):
        if x % 3 == 0 or x % 5 == 0:
            a += x
    print(a)


#  решил сам

summ_3_5(10)