def patternnaivesearch(text, pattern):
    m = len(text)
    n = len(pattern)
    for i in range(m-n+1):
        j = 0
        while j<n and text[i+j]==pattern[j]:
            j+=1
        if j == n:
            return f"Pattern found at index {i}"
        
    return 'pattern not found'
text = input()
pattern = input()
print(patternnaivesearch(text,pattern))