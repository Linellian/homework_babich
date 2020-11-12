def ft_rmstrchar(str, less):
    r = ""
    for i in str:
        if i not in less:
            r += i
        elif i in less:
            r += ""
    str = r
    return str
