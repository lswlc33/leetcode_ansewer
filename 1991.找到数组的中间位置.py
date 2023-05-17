# 给你一个下标从 0 开始的整数数组 nums ，请你找到 最左边 的中间位置 middleIndex （也就是所有可能中间位置下标最小的一个）。
# 中间位置 middleIndex 是满足 nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1] 的数组下标。
# 如果 middleIndex == 0 ，左边部分的和定义为 0 。类似的，如果 middleIndex == nums.length - 1 ，右边部分的和定义为 0 。
# 请你返回满足上述条件 最左边 的 middleIndex ，如果不存在这样的中间位置，请你返回 -1 。



def findMiddleIndex(nums):   
    for i in range(len(nums)):  # 遍历数组的索引
        if sum(nums[ : i]) == sum(nums[i + 1 : ]): ## 对比当前索引的左边和与右边和
            return i
    if sum(nums) - nums[-1] == 0: # 在最左边和最右边的情况
        return len(nums) - 1
    elif sum(nums) - nums[0]  == 0:
        return 0
    return -1 


# 上面多虑了
def findMiddleIndex(nums):
    for i in range(len(nums)):
        if sum(nums[:i])==sum(nums[i+1:]):
            return i
    return -1