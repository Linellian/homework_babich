def ft_len(str):
    count = 0
    for i in str:
        count += 1
    return count


def ft_join(lst, sepp=" "):
    r = ""
    for i in range(ft_len(lst) - 1):
        r += str(lst[i])
        r += sepp
    r += str(lst[-1])
    return r
