def ft_count_char_in_str(char, str):
    c = 0
    for i in str:
        if i == char:
            c += 1
    return c
