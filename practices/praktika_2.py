# Лабораторная работа 2. Ветвления

print("Выберите задание от 1 до 10")
nomer = int(input("Номер задания: "))

# Задание 1
if nomer == 1:
    a = int(input("A: "))
    b = int(input("B: "))
    if a != b:
        bolshe = max(a, b)
        a = bolshe
        b = bolshe
    else:
        a = 0
        b = 0
    print("A =", a, "B =", b)

# Задание 2
elif nomer == 2:
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    c = float(input("Третье число: "))
    minst = min(a, b, c)
    print("Сумма двух наибольших =", a + b + c - minst)

# Задание 3
elif nomer == 3:
    ax = float(input("Ax: "))
    ay = float(input("Ay: "))
    bx = float(input("Bx: "))
    by = float(input("By: "))
    cx = float(input("Cx: "))
    cy = float(input("Cy: "))
    ab = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
    ac = ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5
    if ab < ac:
        print("Ближе точка B, расстояние =", ab)
    else:
        print("Ближе точка C, расстояние =", ac)

# Задание 4
elif nomer == 4:
    x = float(input("x: "))
    y = float(input("y: "))
    if x > 0 and y > 0:
        print("1 четверть")
    elif x < 0 and y > 0:
        print("2 четверть")
    elif x < 0 and y < 0:
        print("3 четверть")
    else:
        print("4 четверть")

# Задание 5
elif nomer == 5:
    x = int(input("Целое число: "))
    if x == 0:
        print("нулевое число")
    else:
        if x > 0:
            znak = "положительное"
        else:
            znak = "отрицательное"
        if x % 2 == 0:
            chet = "четное"
        else:
            chet = "нечетное"
        print(znak, chet, "число")

# Задание 6
elif nomer == 6:
    x = int(input("Число от 1 до 999: "))
    if x % 2 == 0:
        chet = "четное"
    else:
        chet = "нечетное"
    if x < 10:
        razr = "однозначное"
    elif x < 100:
        razr = "двузначное"
    else:
        razr = "трехзначное"
    print(chet, razr, "число")

# Задание 7
elif nomer == 7:
    den = int(input("День (1-31): "))
    mes = int(input("Месяц (1-12): "))
    dni = [
        "первое", "второе", "третье", "четвертое", "пятое",
        "шестое", "седьмое", "восьмое", "девятое", "десятое",
        "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое",
        "шестнадцатое", "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое",
        "двадцать первое", "двадцать второе", "двадцать третье", "двадцать четвертое", "двадцать пятое",
        "двадцать шестое", "двадцать седьмое", "двадцать восьмое", "двадцать девятое", "тридцатое",
        "тридцать первое",
    ]
    mesyacy = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря",
    ]
    print(dni[den - 1], mesyacy[mes - 1])

# Задание 8
elif nomer == 8:
    n = int(input("Число заданий (10-40): "))
    edinicy = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    desyatki = ["", "", "двадцать", "тридцать", "сорок"]
    ot_10_do_19 = [
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
        "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать",
    ]
    if 10 <= n <= 19:
        slovo = ot_10_do_19[n - 10]
    else:
        d = n // 10
        e = n % 10
        if e == 0:
            slovo = desyatki[d]
        elif e == 1:
            slovo = desyatki[d] + " одно"
        elif e == 2:
            slovo = desyatki[d] + " два"
        else:
            slovo = desyatki[d] + " " + edinicy[e]
    ost = n % 10
    if 11 <= n % 100 <= 14:
        forma = "учебных заданий"
    elif ost == 1:
        forma = "учебное задание"
    elif 2 <= ost <= 4:
        forma = "учебных задания"
    else:
        forma = "учебных заданий"
    print(slovo, forma)

# Задание 9
elif nomer == 9:
    n = int(input("Число от 100 до 999: "))
    sotni_slova = [
        "", "сто", "двести", "триста", "четыреста", "пятьсот",
        "шестьсот", "семьсот", "восемьсот", "девятьсот",
    ]
    des_slova = [
        "", "", "двадцать", "тридцать", "сорок", "пятьдесят",
        "шестьдесят", "семьдесят", "восемьдесят", "девяносто",
    ]
    edin_slova = [
        "", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
    ]
    teen_slova = [
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
        "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать",
    ]
    s = n // 100
    d = (n // 10) % 10
    e = n % 10
    chasti = [sotni_slova[s]]
    if d == 1:
        chasti.append(teen_slova[e])
    else:
        if d != 0:
            chasti.append(des_slova[d])
        if e != 0:
            chasti.append(edin_slova[e])
    print(" ".join(chasti))

# Задание 10
elif nomer == 10:
    god = int(input("Год: "))
    # 1984 — год зеленой крысы, начало цикла
    sdvig = god - 1984
    cveta = ["зелен", "красн", "желт", "бел", "черн"]
    zhivotnye = [
        "крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
        "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи",
    ]
    # тигр, заяц, дракон — мужской род
    muzhskoy = {2, 3, 4}
    nomer_zhiv = sdvig % 12
    nomer_cveta = (sdvig % 10) // 2
    osnova = cveta[nomer_cveta]
    if nomer_zhiv in muzhskoy:
        prilag = osnova + "ого"
    else:
        prilag = osnova + "ой"
    print("год", prilag, zhivotnye[nomer_zhiv])

else:
    print("Нет такого задания")

