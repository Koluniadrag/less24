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


def are_brackets_balanced(sequence):
    stack = Stack()

    for char in sequence:
        if char == '(' or char == '{':
            stack.push(char)
        elif char == ')' or char == '}':
            if stack.is_empty():
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{'):
                return False

    return stack.is_empty()

sequence = input("Введіть послідовність символів: ")

if are_brackets_balanced(sequence):
    print("Дужки є сбалансованими.")
else:
    print("Дужки не є сбалансованими.")
