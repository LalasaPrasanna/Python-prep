def Ones(nums):
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                res+=1
                count = max(count,res)
            else:
                res = 0
        return count
nums = [1,0,1,1,0,1]
print(Ones(nums))