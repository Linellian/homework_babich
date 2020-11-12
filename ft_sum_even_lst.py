def ft_sum_even_lst(lst):
    r = 0
    for i in range(0, len(lst), 2):
        r += lst[i]
    return r
