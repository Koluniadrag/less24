class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def reverse_input():
    stack = Stack()


    sequence = input("Введіть послідовність символів: ")


    for char in sequence:
        stack.push(char)

    print("Символи у зворотньому порядку:")
    while not stack.is_empty():
        print(stack.pop(), end="")

    print()

reverse_input()
