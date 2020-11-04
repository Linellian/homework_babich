def ft_even_index_list(mass):
    res = list()
    for i in range(len(mass)):
        if i % 2 == 0:
            res.append(mass[i])
    return res
