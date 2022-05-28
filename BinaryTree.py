class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_input_koren():
    x = int(input("Введите корень дерева: "))
    return x


def get_input_tree_number():
    print("Введите 6 чисел через пробел: ")
    a1, a2, a3, a4, a5, a6 = map(int, input().split())
    return a1, a2, a3, a4, a5, a6


def pre_order(node):
    if node:
        print(node.data)
        pre_order(node.left)
        pre_order(node.right)


class CreateTree(Node):
    x = get_input_koren()
    a1, a2, a3, a4, a5, a6 = get_input_tree_number()

    tree = Node(x)

    def create(self):
        self.tree.left = Node(self.a1)
        self.tree.right = Node(self.a2)
        self.tree.left.left = Node(self.a3)
        self.tree.left.right = Node(self.a4)
        self.tree.right.left = Node(self.a5)
        self.tree.right.right = Node(self.a6)

    def print_tree(self):
        pre_order(self.tree)


def main():
    obj = CreateTree(Node)
    obj.create()
    obj.print_tree()


if __name__ == '__main__':
    main()
