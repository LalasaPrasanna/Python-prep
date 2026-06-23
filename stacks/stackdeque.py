from collections import deque
def stackdeque():
    stack = deque()
    stack.append('A')
    print(stack.pop())
    stack.append('B')
    print(stack[-1])
    return len(stack)
print(stackdeque())