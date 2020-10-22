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

def ft_reverse_str(str):
    l = ft_len(str)
    r = ""
    for i in range(l - 1, -1, -1):
        r = r + str[i]
    return r

def ft_analysis(str):
    print(str[2])
    print(str[-2])
    print(ft_slice_str(str ,0, 6 ))
    print(str[:-2])
    r = ""
    for i in range(ft_len(str)):
        if i % 2 == 0:
            r += str[i]
    print(r)
    r = ""
    for i in range(ft_len(str)):
        if i % 2 != 0:
            r += str[i]
    print(r)
    print(ft_reverse_str(str))
    r = ""
    i = 0
    while i != ft_len(str):
        if i % 2 == 0:
            r += str[ft_len(str) - i - 1]
        i += 1
    print(r)
    print(ft_len(str))

