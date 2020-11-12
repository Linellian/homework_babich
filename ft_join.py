def ft_len(lst):
    c = 0
    for i in lst:
        c += 1
    return c


def ft_join(lst, sep = " "):
    r = ""
    for i in range(ft_len(lst) - 1):
        r += str(lst[i])
        r += sep
    r += str(lst[-1])
    return r
