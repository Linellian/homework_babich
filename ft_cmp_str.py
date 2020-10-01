def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_cmp_str(str1, str2, num):
    l = ft_len(str1)
    r = ""
    for i in range(num - 1):
        r += str1[i]
    r += str2
    for i in range(num - 1, l):
        r += str1[i]
    return r
