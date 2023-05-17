# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

nums = [1,1,0,1,1,1]

def findMaxConsecutiveOnes1(nums):
    r = a = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            a += 1
            if a > r:
                r = a
        else:
            a = 0
    return r

def findMaxConsecutiveOnes2(nums):
    a = 0
    b = -1
    r = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            a = i
        else:
            b = i
        r = max(r, a - b)
    return r