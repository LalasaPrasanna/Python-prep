def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i]==key:
            return f"{key} is found at index {i}"
            break
    else:
        return "Key not found!"
arr = list(map(int, input().split()))
key = int(input())
print(linear_search(arr, key))