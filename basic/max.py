def max(arr):
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    return maxi
arr = list(map(int, input().split()))
print(max(arr))
