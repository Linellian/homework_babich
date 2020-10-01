def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_find_str(str1, str2):
    for i in range(ft_len(str1)):
        b = 0
        for x in range(ft_len(str2)):
            if str1[i+x] != str2[x]:
                b = 1
        if b == 0:
            return i
    return -1
