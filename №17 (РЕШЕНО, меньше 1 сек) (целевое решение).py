# список слов, из которых состоят любые числа в словарной записи (менее 1 триллиона)
a = ['and', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
     'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
     'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred',
     'thousand', 'million', 'billion']


def list_of_numbers_in_words_less_1000(x):
    b = []
    if 0 < x < 10:
        b += [a[0]] + [a[x]]
        return b
    if 0 < x % 100 < 20:
        b += [a[0]] + [a[x % 100]]
    if x % 100 > 19:
        if x % 10 == 0:
            b += [a[0]] + [a[18 + (x % 100) // 10]]
        else:
            b += [a[0]] + [a[18 + (x % 100) // 10] + a[(x % 100) % 10]]
    if x > 99:
        b = [a[x // 100] + a[28]] + b
    return b


def list_of_numbers_in_words(x):
    h = 0
    if len(str(x)) > 12:
        return 'number more than 999 billion'
    for i in range(1, x + 1):
        b = []
        u = i
        b = list_of_numbers_in_words_less_1000(u % 1000) + b
        u //= 1000
        s = 0
        while u > 0:
            b = [a[29 + s]] + b
            b = list_of_numbers_in_words_less_1000(u % 1000) + b
            u //= 1000
            s += 1
        if b[0] == a[0]:
            b.pop(0)
        h += len(''.join(b))
    print(h)

# решил сам
list_of_numbers_in_words(100000)