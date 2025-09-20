def abc(s):
    if s == s[::-1]:
        return 'palindrome'
    else:
        return 'Not palindrome'
s = input()
print(abc(s))