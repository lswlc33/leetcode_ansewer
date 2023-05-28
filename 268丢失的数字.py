def missingNumber(nums):
    n = len(nums) + 1
    for i in range(n):
        if i not in nums:
            return i
        
def missingNumber1(nums):
    nums.sort()
    n = len(nums)
    
    for i in range(n):
        if nums[i] != i:
            return i

    return nums[-1] + 1