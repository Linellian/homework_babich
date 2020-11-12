def ft_join(lst, sep = " "):
    r = ""
    for i in range(len(lst) - 1):
        r += str(lst[i])
        r += sep
    r += str(lst[-1])
    return r
