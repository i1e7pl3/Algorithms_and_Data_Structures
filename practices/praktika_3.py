# Лабораторная работа 3. Циклы

print("Выберите задание от 1 до 10")
nomer = int(input("Номер задания: "))

# Задание 1
if nomer == 1:
    cena = float(input("Цена 1 кг конфет: "))
    kg = 0.1
    while kg <= 1.01:
        print(round(kg, 1), "кг стоит", round(cena * kg, 2))
        kg = kg + 0.1

# Задание 2
elif nomer == 2:
    n = int(input("N (> 0): "))
    proizv = 1
    i = 1
    while i <= n:
        proizv = proizv * (1 + i / 10)
        i = i + 1
    print("Произведение =", proizv)

# Задание 3
elif nomer == 3:
    n = int(input("N (> 0): "))
    s = 0
    k = 1
    while k <= n:
        s = s + (2 * k - 1)
        print("После слагаемого", 2 * k - 1, "сумма =", s)
        k = k + 1
    print("N в квадрате =", s)

# Задание 4
elif nomer == 4:
    a = float(input("A: "))
    n = int(input("N (> 0): "))
    s = 0
    stepen = 1
    i = 0
    while i <= n:
        s = s + stepen
        stepen = stepen * a
        i = i + 1
    print("Сумма =", s)

# Задание 5
elif nomer == 5:
    a = float(input("A: "))
    n = int(input("N (> 0): "))
    s = 0
    stepen = 1
    znak = 1
    i = 0
    while i <= n:
        s = s + znak * stepen
        stepen = stepen * a
        znak = -znak
        i = i + 1
    print("Значение =", s)

# Задание 6
elif nomer == 6:
    a = int(input("A: "))
    b = int(input("B (больше A): "))
    x = a
    while x <= b:
        k = 1
        while k <= x:
            print(x)
            k = k + 1
        x = x + 1

# Задание 7
elif nomer == 7:
    a = float(input("A: "))
    b = float(input("B (меньше A): "))
    ostatok = a
    while ostatok >= b:
        ostatok = ostatok - b
    print("Незанятая часть =", ostatok)

# Задание 8
elif nomer == 8:
    n = int(input("N (> 1): "))
    k = 0
    s = 0
    while s < n:
        k = k + 1
        s = s + k
    print("K =", k)
    print("Сумма =", s)

# Задание 9
elif nomer == 9:
    p = float(input("P процентов (0 < P < 25): "))
    s = 1000
    k = 0
    while s <= 1100:
        k = k + 1
        s = s + s * p / 100
    print("Месяцев K =", k)
    print("Вклад S =", s)

# Задание 10
elif nomer == 10:
    a = int(input("A: "))
    b = int(input("B: "))
    while b != 0:
        ost = a % b
        a = b
        b = ost
    print("НОД =", a)

else:
    print("Нет такого задания")

