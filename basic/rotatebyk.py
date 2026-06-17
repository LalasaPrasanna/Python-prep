k = int(input())
arr = list(map(int,input().split()))
arr = arr[k:]+arr[:k]
print(arr)