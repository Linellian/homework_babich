def ft_sl_list(mass):
    c = 0
    for i in range(1, len(mass)):
        if mass[i] > mass[i - 1]:
            c += 1
    return c
