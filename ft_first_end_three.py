def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_first_end_three(str):
    l = ft_len(str)
    if l <= 5:
        for i in range(l - 1):
            print(str[0], end="")
        print(str[0])
    else:
        print(str[0] + str[1] + str[2] + str[l - 3] + str[l - 2] + str[l - 1])