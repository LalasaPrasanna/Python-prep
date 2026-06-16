def fai(arr):
    res = []
    for i in arr:
        k, l = 0, len(i) - 1
        while k < l:
            i[k], i[l] = i[l], i[k]
            k += 1
            l -= 1
        res.append(i)

    for i in res:
        for idx in range(len(i)):
            i[idx] = 1 - i[idx]

    return res
arr=[[1,0,0],[1,0,1],[0,0,0]]
print(fai(arr))