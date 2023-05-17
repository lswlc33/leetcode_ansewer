# 集合对比法
def containsDuplicate1(nums):
    tem = list(set(nums))
    if sorted(tem) == sorted(nums):
    # 排序太慢了，直接比较长度好些
    # if len(tem) == len(nums):        
        return False

    return True



# 集合算数法
# count太慢了，超时了
def containsDuplicate2(nums):
    for i in set(nums):
        if nums.count(i) >= 2:
            return True
    return False

# 排序看重法
def containsDuplicate3(nums):
    nums = sorted(nums)
    tem = ''
    for i in nums:
        if tem == i:
            return True
        tem = i
    return False


# 字典存放法
def containsDuplicate4(nums):
    dict = {}

    # 遍历一遍添加字典元素
    for num in nums:
        if num in dict:
            # 有，加一
            dict[num] += 1
        else:
            # 没有，创建
            dict[num] = 1

    for i in dict:
        # 看看有没有次数大于1的
        if dict[i] > 1:
            return True
            
        return False