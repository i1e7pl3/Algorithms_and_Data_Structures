# Лабораторная работа 10. Бинарный поиск
# Работает только с отсортированным массивом.
# Каждый раз берем середину и отбрасываем половину.

print("Отсортированный массив введите через пробел")
a = list(map(int, input().split()))
x = int(input("Что ищем: "))

# Задание: бинарный поиск
left = 0
right = len(a) - 1
index = -1

while left <= right:
    seredina = (left + right) // 2
    print("Границы:", left, "-", right, "середина =", seredina, "значение =", a[seredina])
    if a[seredina] == x:
        index = seredina
        print("Нашли на позиции", index)
        break
    if a[seredina] > x:
        print("Искомое меньше, берем левую половину")
        right = seredina - 1
    else:
        print("Искомое больше, берем правую половину")
        left = seredina + 1

if index == -1:
    print("Элемент не найден, ответ -1")
else:
    print("Индекс =", index)
