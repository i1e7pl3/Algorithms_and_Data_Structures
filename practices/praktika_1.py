# Лабораторная работа 1. Линейные алгоритмы

print("Выберите задание от 1 до 12")
nomer = int(input("Номер задания: "))

# Задание 1
if nomer == 1:
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    s = a * b
    p = 2 * (a + b)
    print("Площадь S =", s)
    print("Периметр P =", p)

# Задание 2
elif nomer == 2:
    d = float(input("Диаметр d: "))
    pi = 3.14
    l = pi * d
    print("Длина окружности L =", l)

# Задание 3
elif nomer == 3:
    a = float(input("Число a: "))
    b = float(input("Число b: "))
    srednee = (a + b) / 2
    print("Среднее арифметическое =", srednee)

# Задание 4
elif nomer == 4:
    a = float(input("Число a (не 0): "))
    b = float(input("Число b (не 0): "))
    print("Сумма квадратов =", a ** 2 + b ** 2)
    print("Разность квадратов =", a ** 2 - b ** 2)
    print("Произведение квадратов =", a ** 2 * b ** 2)
    print("Частное квадратов =", a ** 2 / b ** 2)

# Задание 5
elif nomer == 5:
    a = float(input("Число a (не 0): "))
    b = float(input("Число b (не 0): "))
    print("Сумма модулей =", abs(a) + abs(b))
    print("Разность модулей =", abs(a) - abs(b))
    print("Произведение модулей =", abs(a) * abs(b))
    print("Частное модулей =", abs(a) / abs(b))

# Задание 6
elif nomer == 6:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    rasst = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print("Расстояние =", rasst)

# Задание 7
elif nomer == 7:
    a = float(input("Точка A: "))
    b = float(input("Точка B: "))
    c = float(input("Точка C: "))
    ac = abs(c - a)
    bc = abs(c - b)
    print("AC =", ac)
    print("BC =", bc)
    print("Сумма =", ac + bc)

# Задание 8
elif nomer == 8:
    a = float(input("Точка A: "))
    b = float(input("Точка B: "))
    c = float(input("Точка C (между A и B): "))
    ac = abs(c - a)
    bc = abs(c - b)
    print("Произведение AC * BC =", ac * bc)

# Задание 9
elif nomer == 9:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    shirina = abs(x2 - x1)
    vysota = abs(y2 - y1)
    print("Периметр =", 2 * (shirina + vysota))
    print("Площадь =", shirina * vysota)

# Задание 10
elif nomer == 10:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))
    ab = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    bc = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    ac = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    p = ab + bc + ac
    pp = p / 2
    s = (pp * (pp - ab) * (pp - bc) * (pp - ac)) ** 0.5
    print("Периметр =", p)
    print("Площадь =", s)

# Задание 11
elif nomer == 11:
    x = float(input("x: "))
    y = 3 * x ** 6 - 6 * x ** 2 - 7
    print("y =", y)

# Задание 12
elif nomer == 12:
    x = float(input("x: "))
    t = x - 3
    y = 4 * t ** 6 - 7 * t ** 3 + 2
    print("y =", y)

else:
    print("Нет такого задания")

