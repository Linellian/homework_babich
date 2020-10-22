def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_slice_str(str, start, end):
    l = ft_len(str)
    r = ""
    if end > l - 1:
        for i in range(2, l):
            r += str[i]
    else:
        for i in range(start, end - 1):
            r += str[i]
    return r
