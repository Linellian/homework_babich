def ft_odd_even_separator_lst(lst):
    ev = []
    nev = []
    for i in lst:
        if i % 2 == 0:
            ev.append(i)
        else:
            nev.append(i)
    lst = []
    lst.append(ev)
    lst.append(nev)
    return lst
