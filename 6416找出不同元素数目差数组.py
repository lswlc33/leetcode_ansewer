# 给你一个下标从 0 开始的数组 nums ，数组长度为 n 。
# nums 的 不同元素数目差 数组可以用一个长度为 n 的数组 diff 表示，其中 diff[i] 等于前缀 nums[0, ..., i] 中不同元素的数目减去 后缀 nums[i + 1, ..., n - 1] 中不同元素的数目。
# 返回 nums 的 不同元素数目差 数组。
# 注意 nums[i, ..., j] 表示 nums 的一个从下标 i 开始到下标 j 结束的子数组（包含下标 i 和 j 对应元素）。特别需要说明的是，如果 i > j ，则 nums[i, ..., j] 表示一个空子数组。



def distinctDifferenceArray(nums = [1,2,3,4,5]):
    diff = [""] * len(nums)
    for i in range(len(nums)):
        diff[i] = len(set(nums[0:i+1])) - len(set(nums[i+1:len(nums)]))
    return diff

