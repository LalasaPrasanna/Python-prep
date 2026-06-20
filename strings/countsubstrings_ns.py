def count_substrings(text,pattern):
    m,n = len(text),len(pattern)
    count = 0
    for i in range(m-n+1):
        j = 0
        while j<n and text[i+j]==pattern[j]:
            j+=1
        if j==n:
            count +=1
    return count
text = input()
pattern = input()
print(count_substrings(text,pattern))