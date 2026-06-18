
res = []
def targetsum(arr, target):
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if arr[i]+arr[j] == target:
                res.append((arr[i],arr[j]))
    return res
arr = list(map(int,input().split()))
target = int(input())
print(targetsum(arr,target))