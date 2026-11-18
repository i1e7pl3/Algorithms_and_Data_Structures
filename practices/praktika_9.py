# Лабораторная работа 9. Сортировка выбором
# На каждом шаге ищем минимальный элемент в неотсортированной части
# и ставим его на текущее место.

print("Исходный массив введите через пробел")
a = list(map(int, input().split()))
n = len(a)
print("Было:", a)

# Задание: сортировка выбором
i = 0
while i < n - 1:
    min_index = i
    print("--- ищем минимум начиная с позиции", i, "---")
    j = i + 1
    while j < n:
        if a[j] < a[min_index]:
            min_index = j
        j = j + 1
    print("  минимум =", a[min_index], "на позиции", min_index)
    if min_index != i:
        t = a[i]
        a[i] = a[min_index]
        a[min_index] = t
        print("  поменяли с", a[min_index], "->", a)
    else:
        print("  уже на месте ->", a)
    i = i + 1

print("Отсортировано:", a)
