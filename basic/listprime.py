import math
arr = list(map(int,input().split()))
res = []
for i in arr:
    if i ==2 or i ==3:
        res.append(i)
    elif i%2==0 or i%3 == 0:continue
    else:
        for j in range(5, int(math.sqrt(i)),6):
            if i%j == 0:
                continue
        res.append(i)
print(res)