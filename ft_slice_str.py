def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_slice_str(str, start, end):
    l = ft_len(str)
    r = ""
    if end > l:
        for i in range(1, l):
            r += str[i]
    else:
        for i in range(start - 1, end):
            r += str[i]
    return r
