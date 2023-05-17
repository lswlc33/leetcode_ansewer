nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
def matrixSum(nums) -> int:
    score = 0
    len1 = len(nums[0])
    while [] in nums:
        li = []
        for i in range(len(nums)):
            li.append(max(nums[i]))
            nums[i].remove(max(nums[i]))
        score += max(li)
    return score

matrixSum(nums)