def listpalindrome(arr):
    l,r = 0, len(arr)-1
    while l<r:
        if arr[l]==arr[r]:
            r-=1
            l+=1
        else:
            return False
    return True
arr = list(map(int,input().split()))
print(listpalindrome(arr))
