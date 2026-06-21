#eat , ate
def anagram(s1,s2):
    if (sorted(s1)==sorted(s2)):
        return True
    return False
s1 = input()
s2 = input()
print(anagram(s1,s2))
    