def ft_odd_even_analysis_lst(lst):
    ev = 0
    nev = 0
    max_ev = 0
    min_ev = 9999999999
    max_nev = 0
    min_nev = 9999999999
    sum_ev = 0
    sum_nev = 0
    for i in lst:
        if i % 2 == 0:
            ev += 1
            sum_ev += i
            if i < min_ev:
                min_ev = i
            if i > max_ev:
                max_ev = i
        elif i % 2 != 0:
            nev += 1
            sum_nev += i
            if i < min_nev:
                min_nev = i
            if i > max_nev:
                max_nev = i
        

    print("Анализ списка:")
    print("Количество четных чисел:", ev, end=",\t\t")
    print("Количество нечетных чисел:", nev)
    print("Максимальная четная цифра:", max_ev, end=",\t\t")
    print("Максимальная нечетная цифра:", max_nev)
    print("Минимальная четная цифра:", min_ev, end=",\t\t")
    print("Минимальная нечетная цифра:", min_nev)
    print("Сумма четных чисел:", sum_ev, end=",\t\t")
    print("Сумма нечетных чисел:", sum_nev)
