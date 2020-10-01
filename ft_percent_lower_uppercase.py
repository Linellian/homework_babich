def ft_percent_lower_uppercase(str):
    l = 0
    u = 0
    for i in str:
        if i >= "a" and i <= "c" or i >= "а" and i <= "я":
            l += 1
        elif i >= "A" and i <= "C" or i >= "А" and i <= "Я":
            u += 1
    return int(l / u)
