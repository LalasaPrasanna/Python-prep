def longestsubstring(s):
    d = {}
    l = 0
    max_length, left = 0,0
    for right, char in enumerate(s):
        if char in d and d[char]>=left:
            left = d[char]+1
        d[char] = right
        max_length = max(max_length, right-left +1)
    return max_length
s = input()
print(longestsubstring(s))