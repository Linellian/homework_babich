def ft_len(str):
    count = 0
    for i in str:
        count += 1
    return count


def ft_join(l, sepp=" "):
    r = ""
    b = 0
    if not sepp:
        sepp = " "
    while b != ft_len(s) - 1:
        r += l[b] + sepp
    r = r + l[-1]
    return r
