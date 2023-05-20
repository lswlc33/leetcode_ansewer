
nums = [3,2,3]
target = 6

# 暴力法，很慢
def twoSum1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

def twoSum2(nums, target):
    tem = sorted(nums)
    a = b = 0
    while a < len(nums):
        if a != b:
            if tem[a] + tem[b] > target:
                a += 1
            elif tem[a] + tem[b] < target:
                b += 1
            else:
                if tem[a] == tem[b] :
                    c = nums.index(tem[b])
                    nums.remove(tem[b])
                    d = nums.index(tem[a])
                    return c, d
                return nums.index(tem[b]), nums.index(tem[a])
        else:
            a += 1
     
print(twoSum2(nums, target))