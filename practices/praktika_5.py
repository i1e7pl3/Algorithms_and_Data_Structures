# Лабораторная работа 5. Одномерные массивы

print("Выберите задание от 1 до 10")
nomer = int(input("Номер задания: "))

# Задание 1
if nomer == 1:
    n = int(input("N: "))
    a = []
    i = 0
    while i < n:
        a.append(2 * i + 1)
        i = i + 1
    print(a)

# Задание 2
elif nomer == 2:
    n = int(input("N: "))
    a = float(input("A: "))
    d = float(input("D: "))
    massiv = []
    i = 0
    while i < n:
        massiv.append(a * d ** i)
        i = i + 1
    print(massiv)

# Задание 3
elif nomer == 3:
    n = int(input("N: "))
    a = int(input("A: "))
    b = int(input("B: "))
    massiv = [a, b]
    i = 2
    while i < n:
        s = 0
        j = 0
        while j < i:
            s = s + massiv[j]
            j = j + 1
        massiv.append(s)
        i = i + 1
    print(massiv)

# Задание 4
elif nomer == 4:
    a = list(map(int, input("Массив через пробел: ").split()))
    n = len(a)
    i = 0
    while i < (n + 1) // 2:
        print(a[i])
        if i != n - 1 - i:
            print(a[n - 1 - i])
        i = i + 1

# Задание 5
elif nomer == 5:
    a = list(map(int, input("Массив через пробел: ").split()))
    n = len(a)
    # нечетные номера (1, 3, 5...) — в Python это индексы 0, 2, 4...
    i = 0
    while i < n:
        print(a[i])
        i = i + 2
    i = n - 1
    if i % 2 == 0:
        i = i - 1
    while i >= 1:
        print(a[i])
        i = i - 2

# Задание 6
elif nomer == 6:
    a = list(map(float, input("Массив через пробел: ").split()))
    k = int(input("K: "))
    l = int(input("L: "))
    s = 0
    i = k - 1
    while i <= l - 1:
        s = s + a[i]
        i = i + 1
    print("Среднее =", s / (l - k + 1))

# Задание 7
elif nomer == 7:
    a = list(map(int, input("Массив через пробел: ").split()))
    n = len(a)
    d = a[1] - a[0]
    ok = True
    i = 2
    while i < n:
        if a[i] - a[i - 1] != d:
            ok = False
        i = i + 1
    if ok:
        print(d)
    else:
        print(0)

# Задание 8
elif nomer == 8:
    a = list(map(int, input("Массив через пробел: ").split()))
    n = len(a)
    # четные номера 2, 4, 6... — индексы 1, 3, 5...
    minst = a[1]
    i = 3
    while i < n:
        if a[i] < minst:
            minst = a[i]
        i = i + 2
    print("Минимум с четными номерами =", minst)

# Задание 9
elif nomer == 9:
    a = list(map(int, input("Массив через пробел: ").split()))
    n = len(a)
    nomer_max = -1
    i = 1
    while i < n - 1:
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            nomer_max = i + 1
        i = i + 1
    print("Номер последнего локального максимума =", nomer_max)

# Задание 10
elif nomer == 10:
    a = list(map(int, input("Массив через пробел: ").split()))
    n = len(a)
    i = 0
    nashli = False
    while i < n and not nashli:
        j = i + 1
        while j < n:
            if a[i] == a[j]:
                print(i + 1, j + 1)
                nashli = True
                break
            j = j + 1
        i = i + 1

else:
    print("Нет такого задания")
