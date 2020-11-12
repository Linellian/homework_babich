def ft_rmstrspc(str):
    r = ""
    for i in str:
        if i != " ":
            r += i
        elif i == " ":
            r += ""
    str = r
    return str
