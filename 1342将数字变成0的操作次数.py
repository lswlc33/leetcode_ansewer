# 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

num = 14

# 标准
def solution1(num):
    sp = 0
    temp = num
    while (temp != 0):
        if (temp % 2 == 0):   # 偶数
            temp = temp / 2
        else:       # 奇数
            temp = temp - 1
        sp = sp + 1
    return sp

# python中0代表False，其他数字代表True，利用这个条件当True时执行循环
def solution2(num):
    sp = 0
    while (num):
        if (num % 2 == 0):   # 偶数
            num = num / 2
        else:                # 奇数
            num -= 1
        sp += 1
    return sp

print(solution2(num))