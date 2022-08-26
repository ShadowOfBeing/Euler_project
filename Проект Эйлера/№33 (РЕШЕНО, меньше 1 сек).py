# если задача с подвохом (если условие, что все дроби равны 1/2), то решение следующее:
a1 = 1/2 ** 4  # искомое произведение
a2 = 2 * 4     # искомый знаменатель

# если речь не только про дроби, которые равны 1/2, то решение следующее:
a = [i for i in range(11, 100)]
for i in a:
    if i % 10 == 0:
        a.remove(i)
s1 = 1
s2 = 1
i = 0
while i < len(a) - 1:
    k = i + 1
    while k < len(a):
        if a[i] // 10 == a[i] % 10 and a[k] // 10 == a[k] % 10:
            k += 1
            continue
        elif a[i] / a[k] == (a[i] // 10) / (a[k] % 10):
            s1 *= a[i]
            s2 *= a[k]
        k += 1
    i += 1


def greatest_divisor_s2(a, b):
    for b1 in range(a // 2, 1, -1):
        if a % b1 == 0 and b % b1 == 0:
            b //= b1
            return b
    return b


if s2 % s1 == 0:
    s2 //= s1
else:
    s2 = greatest_divisor_s2(s1, s2)

# решил сам
