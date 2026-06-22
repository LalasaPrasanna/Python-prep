def charactercount(s):
    
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    res = [[i,d[i]] for i in d]
    ans  = ''.join([f'{char}:{count} ' for char,count in res])
    return ans
s = input()
print(charactercount(s))