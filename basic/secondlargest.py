def secondlargest(arr):
    maxi = arr[0]
    sec = 0
    if len(arr)>1:
        for i in arr:
            if i > maxi:
                sec = maxi
                maxi = i
    return sec
arr = list(map(int,input().split()))
print(secondlargest(arr))