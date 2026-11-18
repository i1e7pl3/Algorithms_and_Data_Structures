# Лабораторная работа 4. Рекурсия

print("Выберите задание от 1 до 9")
nomer = int(input("Номер задания: "))

# Задание 1
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Задание 2
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Задание 3
def stepen(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / stepen(x, -n)
    return x * stepen(x, n - 1)

# Задание 4
def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

# Задание 5
def bin_poisk(massiv, x, left, right):
    if left > right:
        return -1
    seredina = (left + right) // 2
    if massiv[seredina] == x:
        return seredina
    if massiv[seredina] > x:
        return bin_poisk(massiv, x, left, seredina - 1)
    return bin_poisk(massiv, x, seredina + 1, right)

# Задание 6
def obratnye_slova(s):
    s = s.strip()
    if " " not in s:
        return s
    pervoe, ostatok = s.split(" ", 1)
    return obratnye_slova(ostatok) + " " + pervoe

# Задание 7
def prostoe(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def summa_prostyh(n):
    if n == 0:
        return []
    p = n
    while p >= 2:
        if prostoe(p):
            return [p] + summa_prostyh(n - p)
        p = p - 1
    return []

# Задание 8
def kolichestvo_cifr(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + kolichestvo_cifr(n // 10)

# Задание 9
def hanoi(n, otkuda, kuda, vspom):
    if n == 1:
        print(otkuda, "->", kuda)
        return
    hanoi(n - 1, otkuda, vspom, kuda)
    print(otkuda, "->", kuda)
    hanoi(n - 1, vspom, kuda, otkuda)

if nomer == 1:
    n = int(input("n: "))
    print("Факториал =", factorial(n))

elif nomer == 2:
    n = int(input("n: "))
    print(n, "-е число Фибоначчи =", fib(n))

elif nomer == 3:
    x = float(input("x: "))
    n = int(input("n: "))
    print("x в степени n =", stepen(x, n))

elif nomer == 4:
    s = input("Строка: ")
    if palindrom(s):
        print("Это палиндром")
    else:
        print("Это не палиндром")

elif nomer == 5:
    massiv = list(map(int, input("Отсортированный массив через пробел: ").split()))
    x = int(input("Искомый элемент: "))
    index = bin_poisk(massiv, x, 0, len(massiv) - 1)
    if index == -1:
        print("Элемент не найден")
    else:
        print("Индекс =", index)

elif nomer == 6:
    s = input("Строка: ")
    print(obratnye_slova(s))

elif nomer == 7:
    n = int(input("Число: "))
    print("Сумма простых =", summa_prostyh(n))

elif nomer == 8:
    n = int(input("Число: "))
    print("Количество цифр =", kolichestvo_cifr(n))

elif nomer == 9:
    n = int(input("Число дисков: "))
    hanoi(n, "A", "C", "B")

else:
    print("Нет такого задания")
