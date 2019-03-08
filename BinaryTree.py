class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_leave = None
        self.right_leave = None

    def insert(self, element):
        if element < self.root:
            if self.left_leave:
                self.left_leave.insert(element)
            else:
                self.left_leave = element
        elif element > self.right_leave:


    def print_tree(self):
        if self.left_leave:
            self.left_leave.print_tree()
        print(self.root)
        if self.right_leave:
            self.right_leave.print_tree()


if __name__ =='__main__':
