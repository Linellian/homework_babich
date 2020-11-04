def ft_rev_list(mass):
    for i in range(len(mass) - 1, -1, -1):
        mass.append(mass.pop(i))
    return mass
