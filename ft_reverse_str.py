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
