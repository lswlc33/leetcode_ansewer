# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
# 请返回 nums 的动态和。


nums = [1,2,3,4]

# 传统逐一计算加入新列表
def solution1 (nums):
    dp = []
    b = 0
    for i in nums:
        b = b + i
        dp.append(b)
    return dp

# 创建同长度列表遍历覆写
def solution2(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1,len(dp)):
        dp[i] = dp[i - 1] + nums[i]
    return dp




print(solution2(nums))