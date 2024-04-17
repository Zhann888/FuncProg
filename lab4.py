#13 - Написать функцию для рекурсивного поиска или вставки элемента в бинарное дерево поиска.
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + " Not Found"
            return self.left.find(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " Not Found"
            return self.right.find(val)
        else:
            print(str(self.data) + ' is found')

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find(5))
print(root.find(14))
print(root.PrintTree())
