def plusOne(digits):
    # 最后一位加一
    digits[-1] += 1

    # 如果数据到达10就进位
    while 10 in digits:

        i = digits.index(10)
        digits[i] = 0

        # 前一位加一
        if i - 1 >= 0:
            digits[i - 1] += 1
        else:
            digits = [1] + digits
            
    # 返回
    return digits

def plusOne2(digits):

    num = ""

    # 转字符串
    for i in digits:
        num = num + str(i)

    r = []

    # 加一后在转int到列表输出
    for i in str(int(num) + 1):
        r.append(int(i))
    return r

