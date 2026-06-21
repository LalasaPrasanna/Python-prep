def palindrome(s):
    i,j = 0, len(s)-1
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
            continue
        else:
            return False
    return True
s = input()
print(palindrome(s)) 
            