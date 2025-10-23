n = input()
d = {}
for i in n:
    if i not in d:
        d[i]= 1
    else:
        d[i]+=1
for i in d:
    if d[i]==1:
        break
print(i)
    