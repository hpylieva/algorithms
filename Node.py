class Node:
    def __init__(self, root):
        self.root = root
        self.left_leave = None
        self.right_leave = None

    def insert(self, element):
        if element < self.root:
            if self.left_leave:
                self.left_leave.insert(element)
            else:
                self.left_leave = Node(element)
        elif element > self.root:
            if self.right_leave:
                self.right_leave.insert(element)
            else:
                self.right_leave = Node(element)
        else:
            raise ValueError('such value already exists!')

    def print_tree(self):
        if self.left_leave:
            self.left_leave.print_tree()
        print(self.root, end=' ')
        if self.right_leave:
            self.right_leave.print_tree()


if __name__ =='__main__':
    tree = Node(11)
    tree.insert(9)
    tree.insert(7)
    tree.insert(15)
    tree.print_tree()
