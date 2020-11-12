def ft_sum_even_part_lst(lst):
    r = 0
    for i in lst:
        if i % 2 == 0:
            r += i
    return r
