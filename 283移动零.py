def moveZeroes(nums):
    a = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[a] = nums[i]
            a += 1
    for i in range(len(nums)-a):
        nums[-1-i] = 0


def moveZeroes(nums):
    a = b = 0
    while a < len(nums):
        if nums[a] != 0:
            nums[a] ,nums[b] = nums[b] ,nums[a]
            b += 1
        a += 1