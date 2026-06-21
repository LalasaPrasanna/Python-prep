def lps_array(pattern, lps):
    i = 1
    l = 0
    m = len(pattern)
    while i<m:
        if pattern[i]==pattern[l]:
            l+=1
            lps[i] = l
            i+=1
        else:
            if l!= 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i+=1
    return lps
def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    lps = [0]*n
    res = []
    lps_array(pattern, lps)
    i = 0
    j = 0
    while i <n:
        if text[i] == pattern[j]:
            i+=1
            j+=1
            if j == m:
                res.append(i-j)
                j = lps[j-1]
        else:
            if j!=0:
                j = lps[j-1]
                i+=1
    return len(res)
pattern = input()
text = input()
print(kmp_search(pattern, text))

