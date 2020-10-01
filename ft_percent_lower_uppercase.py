def ft_percent_lower_uppercase(str):
    l = 0
    u = 0
    for i in str:
        if i >= "a" and i <= "c":
            l += 1
        elif i >= "A" and i <= "C":
            u += 1
    return int(l / u * 100)
