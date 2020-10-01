def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c



def ft_find_str(str1, str2):
    l = ft_len(str1)
    l2 = ft_len(str2)
    for i in range(l):
        c = 0
        for x in range(l2):
            if str1[i + x] != str2[x]:
                c = 1
        if c == 0:
            return i + 1
    return -1
