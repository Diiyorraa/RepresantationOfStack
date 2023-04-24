class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return self.items == []

    def peek(self):
        if not self.empty():
            return self.items[-1]

    def getStack(self):
        return self.items

    def choice(self):
        while True:
            choice = int(input("Please enter choice: "))
            if choice == 1:
                item = int(input("Enter num: "))
                self.push(item)
                print(self.getStack())
            if choice == 2:
                self.pop()
                print(self.getStack())
            if choice == 3:
                print(self.peek())
                print(self.getStack())
            if choice == 4:
                print(self.getStack())

obj = Stack()
obj.choice()

