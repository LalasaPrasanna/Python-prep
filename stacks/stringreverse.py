def string_reverse(s):
    stack = []
    for ch in s:
        stack.append(ch)
        reversed_s = ''
    while stack:
            reversed_s += stack.pop()
    return reversed_s
s = input()
print(string_reverse(s))