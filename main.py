# # 13 - Найти квадратный корень каждого числа в списке, отфильтровать те, что больше 2, и найти их сумму
#
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# square = filter(lambda x: x > 2, map(lambda x: x ** 0.5, numbers))
# summ = reduce(lambda x, y: x + y, square)
# print(numbers)
# print(f"result: {summ}")


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)


# Пример использования:

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("Inorder traversal:")
inorder_traversal(r)
