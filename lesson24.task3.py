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

    def get_from_stack(self, e):
        temp_stack = Stack()
        found = False

        while not self.is_empty():
            item = self.pop()
            if item == e:
                found = True
                break
            temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return e
        else:
            raise ValueError("Елемент не знайдено у стеці.")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

try:
    result = stack.get_from_stack(2)
    print("Знайдено:", result)
except ValueError as e:
    print(e)

try:
    result = stack.get_from_stack(5)
    print("Знайдено:", result)
except ValueError as e:
    print(e)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0


