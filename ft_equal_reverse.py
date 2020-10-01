def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_reverse_str(str):
    l = ft_len(str)
    r = ""
    for i in range(l - 1, -1, -1):
        r = r + str[i]
    return r


def ft_equal_reverse(str):
    l = ft_len(str)
    p = ""
    v = ""
    if l % 2 == 0:
        for i in range(l // 2):
            p += str[i]
        for i in range(l // 2, l):
            v += str[i]
    else:
        for i in range(l // 2):
            p += str[i]
        for i in range(l // 2 + 1, l):
            v += str[i]
    return p == ft_reverse_str(v)
