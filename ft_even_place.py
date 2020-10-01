def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_even_place(str):
    r = ""
    l = ft_len(str)
    for i in range(l):
        if i % 2 != 0:
            r = r + str[i]
    return r
