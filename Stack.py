import timeit
from timeit import Timer


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def par_balance_checker(input: str) -> bool:
    s = Stack()
    for char in input:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.is_empty():
                return False
            s.pop()
    if s.is_empty():
        return True
    else:
        return False


def _match(left_char, right_char):
    left_char_list = '[{('
    right_char_list = ']})'
    return left_char_list.index(left_char) == right_char_list.index(right_char)


def char_balance_checker(input: str) -> bool:
    s = Stack()
    for char in input:
        if char in '([{':
            s.push(char)
        elif char in ')}]':
            if s.is_empty():
                return False
            if not _match(s.pop(), char):
                return False
    if s.is_empty():
        return True
    else:
        return False


def dec_to_binary(dec_number: int) -> str:
    remstack = Stack()
    while dec_number > 0:
        remstack.push(dec_number % 2)
        dec_number = dec_number // 2
    binary = ''
    while not remstack.is_empty():
        binary = binary + str(remstack.pop())
    return binary


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while dec_number > 0:
        remstack.push(dec_number % base)
        dec_number = dec_number // base

    newString = ""
    while not remstack.is_empty():
        newString = newString + digits[remstack.pop()]

    return newString

if __name__ == '__main__':
    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

    print(par_balance_checker('(((aaa)b)a)'))
    print(par_balance_checker('(()'))
    print(par_balance_checker('())'))

    print(char_balance_checker('(([aaa]b)a)'))
    print(char_balance_checker('(()]'))
    print(char_balance_checker('{{([][])}()}'))
    i = 8
    print(dec_to_binary(i))
    print(i) # changes in module don't affect input value
    print(dec_to_binary(42))

    t1 = Timer("dec_to_binary(42)", "from Stack import dec_to_binary")
    print("my ", t1.timeit(number=1000), "milliseconds")

    print(base_converter(31, 16))
    print(base_converter(31, 2))
    print(base_converter(256, 16))
    print(base_converter(25, 8))
