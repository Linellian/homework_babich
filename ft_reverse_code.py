def ft_reverse_code(a):
    ch = a
    if a > 0:
        r = ''
        while a > 0:
            y = str(a % 2)
            r = y + r
            a = int(a / 2)
        while len(r) != 8:
            r = '0' + r
    else:
        a = a * -1
        r = ''
        while a > 0:
            y = str(a % 2)
            r = y + r
            a = int(a / 2)
        while len(r) != 7:
            r = '0' + r
        r = '1' + r
    x = '1'
    if ch > 0:
        return r
    else:
        for i in r[1:]:
            if i == '0':
                x = x + '1'
            else:
                x = x + '0'
        return x
