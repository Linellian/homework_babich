def ft_len(str):
    num = 0
    for i in str:
        num += 1
    return num


def ft_sum_even_lst(lst):
    r = 0
    for i in range(ft_len(lst) - 1):
        if i % 2 == 0:
            r += lst[i]
    return r
