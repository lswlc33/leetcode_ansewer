# 给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
# 返回该 最大总和 。

nums = [1,4,3,2]


def arrayPairSum(nums):
    return sum(sorted(nums)[::2])

