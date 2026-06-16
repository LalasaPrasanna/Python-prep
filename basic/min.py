def min(arr):
    mini = arr[0]
    for i in arr:
        if i < mini:
            mini = i
    return mini
arr = [11,2,3,10,5]
print(min(arr))