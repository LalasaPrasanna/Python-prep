class stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
        return self.items
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
a = stack()
print(a.size())
print(a.push('A'))
print(a.push('B'))
print(a.push('C'))
print(a.pop())
print(a.size())
print(a.is_empty())