# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。


## 遍历找结果
def sol1(nums, target):
    for i in range(len(nums)):
        if target < nums[0]:
            return 0
        if target <=nums[i]:
            return i
    return len(nums)

## 加入源列表排序找索引
def sol2(nums, target):
    nums.append(target)
    return sorted(nums).index(target)

## 还有个二分查找法，懒得看了