from LinkedList import ListNode

if __name__ == '__main__':
    dummyHead = ListNode(0)
    a = dummyHead
    for i in [2, 4, 3]:
        a.next = ListNode(i)
        a = a.next
    # dummyHead.next now is a linked list with values 2,4,3

    # analogy
    l = [0, []]
    c = l
    print(f'l: {l}, c: {c}')
    c[1] = [2, []]
    c = c[1]
    print(f'l: {l}, c: {c}')
    c[1] = [3, []]
    c = c[1]
    print(f'l: {l}, c: {c}')
