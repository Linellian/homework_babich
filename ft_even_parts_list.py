def ft_eben_parts_list(mass):
    res = list()
    for i in mass:
        if i % 2 == 0:
            res.append(i)
    return res
