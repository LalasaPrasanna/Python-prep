def makeFancyString( s):
        res = ''
        count = 0

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1 

            if count <= 2:
                res += s[i]

        return res
s=input()
print(makeFancyString(s))