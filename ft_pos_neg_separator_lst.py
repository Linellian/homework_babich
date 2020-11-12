def ft_pos_neg_separator_lst(lst):
    neg = []
    pos = []
    zero = []
    for i in lst:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        elif i == 0:
            zero.append(i)
    lst = []
    lst.append(neg)
    lst.append(zero)
    lst.append(pos)
    return lst
