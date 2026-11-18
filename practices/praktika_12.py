# Лабораторная работа 12. Очередь
# Очередь работает как очередь в магазине: первый пришел — первый вышел (FIFO).

from collections import deque

# Задание: работа с очередью
ochered = deque()
print("Пустая очередь:", list(ochered))

# добавление в конец
print("Добавляем 1, 2, 3")
ochered.append(1)
print("После добавления 1:", list(ochered))
ochered.append(2)
print("После добавления 2:", list(ochered))
ochered.append(3)
print("После добавления 3:", list(ochered))

# просмотр первого без удаления
print("Первый элемент (не удаляем):", ochered[0])

# удаление из начала
pervyi = ochered.popleft()
print("Взяли из очереди:", pervyi)
print("Сейчас очередь:", list(ochered))

print("Размер очереди:", len(ochered))
print("Пустая ли очередь?", len(ochered) == 0)

print("Добавьте свои числа через пробел, они встанут в очередь")
dobavka = list(map(int, input().split()))
i = 0
while i < len(dobavka):
    ochered.append(dobavka[i])
    print("Добавили", dobavka[i], "->", list(ochered))
    i = i + 1

print("Разбираем очередь до конца:")
while len(ochered) > 0:
    x = ochered.popleft()
    print("Вышел", x, "осталось", list(ochered))
