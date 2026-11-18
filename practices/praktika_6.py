# Лабораторная работа 6. Матрицы

print("Выберите задание от 1 до 10")
nomer = int(input("Номер задания: "))


def chitat_matritsu():
    m = int(input("Число строк M: "))
    n = int(input("Число столбцов N: "))
    print("Введите матрицу построчно, числа через пробел")
    a = []
    i = 0
    while i < m:
        stroka = list(map(float, input().split()))
        a.append(stroka)
        i = i + 1
    return a, m, n


# Задание 1
if nomer == 1:
    m = int(input("Порядок M (нечетное): "))
    print("Введите квадратную матрицу")
    a = []
    i = 0
    while i < m:
        a.append(list(map(float, input().split())))
        i = i + 1
    poseshcheno = []
    i = 0
    while i < m:
        poseshcheno.append([False] * m)
        i = i + 1
    # вниз, вправо, вверх, влево
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    napr = 0
    i = 0
    j = 0
    k = 0
    while k < m * m:
        print(a[i][j])
        poseshcheno[i][j] = True
        ni = i + di[napr]
        nj = j + dj[napr]
        if ni < 0 or ni >= m or nj < 0 or nj >= m or poseshcheno[ni][nj]:
            napr = (napr + 1) % 4
            ni = i + di[napr]
            nj = j + dj[napr]
        i = ni
        j = nj
        k = k + 1

# Задание 2
elif nomer == 2:
    a, m, n = chitat_matritsu()
    k = int(input("K: "))
    s = 0
    p = 1
    j = 0
    while j < n:
        s = s + a[k - 1][j]
        p = p * a[k - 1][j]
        j = j + 1
    print("Сумма =", s)
    print("Произведение =", p)

# Задание 3
elif nomer == 3:
    a, m, n = chitat_matritsu()
    luchshiy = 1
    min_p = None
    j = 0
    while j < n:
        p = 1
        i = 0
        while i < m:
            p = p * a[i][j]
            i = i + 1
        if min_p is None or p < min_p:
            min_p = p
            luchshiy = j + 1
        j = j + 1
    print("Номер столбца =", luchshiy)
    print("Произведение =", min_p)

# Задание 4
elif nomer == 4:
    a, m, n = chitat_matritsu()
    j = 0
    while j < n:
        s = 0
        i = 0
        while i < m:
            s = s + a[i][j]
            i = i + 1
        sred = s / m
        kol = 0
        i = 0
        while i < m:
            if a[i][j] > sred:
                kol = kol + 1
            i = i + 1
        print("Столбец", j + 1, ":", kol)
        j = j + 1

# Задание 5
elif nomer == 5:
    a, m, n = chitat_matritsu()
    otvet = 0
    j = 0
    while j < n:
        vse_nechet = True
        i = 0
        while i < m:
            if int(a[i][j]) % 2 == 0:
                vse_nechet = False
            i = i + 1
        if vse_nechet:
            otvet = j + 1
            break
        j = j + 1
    print(otvet)

# Задание 6
elif nomer == 6:
    a, m, n = chitat_matritsu()
    i = 0
    while i < m:
        jmin = 0
        jmax = 0
        j = 1
        while j < n:
            if a[i][j] < a[i][jmin]:
                jmin = j
            if a[i][j] > a[i][jmax]:
                jmax = j
            j = j + 1
        t = a[i][jmin]
        a[i][jmin] = a[i][jmax]
        a[i][jmax] = t
        i = i + 1
    i = 0
    while i < m:
        print(a[i])
        i = i + 1

# Задание 7
elif nomer == 7:
    a, m, n = chitat_matritsu()
    imin = 0
    jmin = 0
    imax = 0
    jmax = 0
    i = 0
    while i < m:
        j = 0
        while j < n:
            if a[i][j] < a[imin][jmin]:
                imin = i
                jmin = j
            if a[i][j] > a[imax][jmax]:
                imax = i
                jmax = j
            j = j + 1
        i = i + 1
    i = 0
    while i < m:
        t = a[i][jmin]
        a[i][jmin] = a[i][jmax]
        a[i][jmax] = t
        i = i + 1
    i = 0
    while i < m:
        print(a[i])
        i = i + 1

# Задание 8
elif nomer == 8:
    a, m, n = chitat_matritsu()
    hm = m // 2
    hn = n // 2
    i = 0
    while i < hm:
        j = 0
        while j < hn:
            t = a[i][j]
            a[i][j] = a[i + hm][j + hn]
            a[i + hm][j + hn] = t
            j = j + 1
        i = i + 1
    i = 0
    while i < m:
        print(a[i])
        i = i + 1

# Задание 9
elif nomer == 9:
    a, m, n = chitat_matritsu()
    i = 0
    while i < m:
        k = i + 1
        while k < m:
            if a[k][0] < a[i][0]:
                t = a[i]
                a[i] = a[k]
                a[k] = t
            k = k + 1
        i = i + 1
    i = 0
    while i < m:
        print(a[i])
        i = i + 1

# Задание 10
elif nomer == 10:
    m = int(input("Порядок M: "))
    print("Введите квадратную матрицу")
    a = []
    i = 0
    while i < m:
        a.append(list(map(float, input().split())))
        i = i + 1
    # диагонали, параллельные главной, начиная с одноэлементной (левый нижний угол)
    d = m - 1
    while d >= -(m - 1):
        s = 0
        i = 0
        while i < m:
            j = i - d
            if 0 <= j < m:
                s = s + a[i][j]
            i = i + 1
        print("Диагональ i - j =", d, "сумма =", s)
        d = d - 1

else:
    print("Нет такого задания")
