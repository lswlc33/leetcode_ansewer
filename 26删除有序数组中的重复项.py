class Solution:
    def removeDuplicates(self, nums):
        a = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                nums[a] = nums[i]
                a += 1
        return a
