def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # store a copy of current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # undo last choice

    backtrack(0, [])
    return result
nums = [1,2,3,4,5]
print(subsets(nums))