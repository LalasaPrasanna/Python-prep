def duplicates_remove(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

arr = list(map(int,input().split()))
print(duplicates_remove(arr))