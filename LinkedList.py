class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def print_list(self):
        print_node = self.headval
        while print_node.next is not None:
            print(print_node.val, end='->')
            print_node = print_node.next
        print(f'{print_node.val}\n\n')

    def insert_front(self, element):
        temp = self.headval
        node_element = ListNode(element)
        self.headval = node_element
        node_element.next = temp

    def insert_end(self, element):
        node_element = ListNode(element)
        if self.headval is None:
            self.headval = node_element
        else:
            list_member = self.headval
            while list_member.next is not None:
                list_member = list_member.next
            list_member.next = node_element

    def remove_by_key(self, key: str):
        prev_member = self.headval
        while prev_member.next.val != key:
            prev_member = prev_member.next
        prev_member.next = prev_member.next.next


if __name__ == '__main__':
    e1 = ListNode('Mon')
    e2 = ListNode('Tue')
    e3 = ListNode('Wed')

    ll = LinkedList()
    ll.headval = e1
    ll.headval.next = e2
    e2.next = e3
    print('Initial list:')
    ll.print_list()

    ll.insert_front('Sun')
    print("Inserted Sun to list:",)
    ll.print_list()

    ll.insert_end('Thu')
    print('Inserted Thu to the end:')
    ll.print_list()

    ll.remove_by_key('Mon')
    print('Removed Mon')
    ll.print_list()
