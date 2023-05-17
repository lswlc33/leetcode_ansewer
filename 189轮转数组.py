# 直接遍历法调包法
def rotate1(nums, k):
    # 算出真正的旋转次数
    k = k % len(nums)
    # 遍历删除并添加
    for i in range(k):
        nums.insert(0, nums.pop())

# 切片拼接法
def rotate2(nums, k):
    # 算出真正的旋转次数
    k = k % len(nums)
    # 切片拼接
    nums = nums[-k:] + nums[:-k]
    # 需要加上[:]才能被通过
    # nums[:] = nums[-k:] + nums[:-k]

# 三次反转法

def rotate3(nums, k):
    k = k % len(nums)
    # 反转数组
    nums[:] = nums[::-1]
    # 反转前半段
    nums[:k] = nums[:k][::-1]
    # 反转后半段
    nums[k:] = nums[k:][::-1]
    