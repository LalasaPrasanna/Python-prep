def subarrayBitwiseORs(arr):
    res = set()
    prev = set()
    
    for num in arr:
        cur = {num}
        for val in prev:
            cur.add(val | num)
        prev = cur
        res.update(cur)
        
    return len(res)
arr=[2,3,1,1]
print(subarrayBitwiseORs(arr))