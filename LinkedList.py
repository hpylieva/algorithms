class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def insert_front(self, element: Node):
        temp = self.headval
        self.headval = element
        element.nextval = temp

    def insert_end(self, element: Node):
        if self.headval is None:
            self.headval = element
        else:
            list_member = self.headval
            while list_member.nextval is not None:
                list_member = list_member.nextval
            list_member.nextval = element

    def remove_by_key(self, key: str):
        prev_member = self.headval
        while prev_member.nextval.dataval != key:
            prev_member = prev_member.nextval
        prev_member.nextval = prev_member.nextval.nextval


if __name__ == '__main__':
    e1 = Node('Mon')
    e2 = Node('Tue')
    e3 = Node('Wed')

    ll = LinkedList()
    ll.headval = e1
    ll.headval.nextval = e2
    e2.nextval = e3
    print('Initial list:')
    ll.print_list()

    ll.insert_front(Node('Sun'))
    print("Inserted Sun to list:")
    ll.print_list()

    ll.insert_end(Node('Thu'))
    print('Inserted Thu to the end:')
    ll.print_list()

    ll.remove_by_key('Mon')
    print('Removed Mon')
    ll.print_list()
