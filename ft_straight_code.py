def ft_straight_code(a):
    if a > 0:
        r = ''
        while a > 0:
            b = str(a % 2)
            r = b + r
            a = int(a / 2)
        while len(r) != 8:
            r = '0' + r
        return r
    else:
        a = a * -1
        r = ''
        while a > 0:
            b = str(a % 2)
            r = b + r
            a = int(a / 2)
        while len(r) != 7:
            r = '0' + r
        r = '1' + r
        return r
