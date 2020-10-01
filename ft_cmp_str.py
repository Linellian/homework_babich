def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_cmp_str(str1, str2, num):
    r = ""
    l = ft_len(str1)
    for i in range(num):
        r += str1[i]
    r += str2
    for i in range(num, l):
        r += str1[i]
    return r
