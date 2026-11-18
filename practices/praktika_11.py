# Лабораторная работа 11. Обход дерева
# Бинарное дерево поиска: меньше — налево, больше или равно — направо.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Задание 1. Вставка в дерево
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


# Задание 2. Поиск в дереве
def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


# Задание 3. Обход слева-корень-справа (по возрастанию)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# Задание 4. Обход корень-лево-право
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Задание 5. Обход лево-право-корень
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


print("Числа для дерева введите через пробел")
chisla = list(map(int, input().split()))

derevo = None
i = 0
while i < len(chisla):
    derevo = insert(derevo, chisla[i])
    i = i + 1

print("Обход inorder (по возрастанию):")
inorder(derevo)
print()

print("Обход preorder:")
preorder(derevo)
print()

print("Обход postorder:")
postorder(derevo)
print()

x = int(input("Какое число искать: "))
if search(derevo, x):
    print("Элемент найден")
else:
    print("Элемент не найден")
