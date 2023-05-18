# 这个remove耗时惊人，好在不超时
def singleNumber1(nums):
    for i in set(nums):
        # 两次remove
        nums.remove(i)
        try:
            # 找不到第二个i啊，那就返回吧
            nums.remove(i)
        except:
            return i
        
def singleNumber2(nums):
    # 排序下
    nums = sorted(nums)

    for i in range(0, len(nums), 2):
        # 用于处理单独的数在最后一个的情况
        if i == len(nums) - 1:
            return nums[i]
        # 如果相邻不同，就返回
        if nums[i] != nums[i + 1]:
            return nums[i]

# 哈希表法    
def singleNumber3(nums):
    dict = {}

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    for i in dict:
        if dict[i] == 1:
            return i
        
# 异或法
def singleNumber4(nums):
    a = 0
    for i in nums:
        a ^= i
    return a