# 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：
# answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
# answer[i] == "Fizz" 如果 i 是 3 的倍数。
# answer[i] == "Buzz" 如果 i 是 5 的倍数。
# answer[i] == i （以字符串形式）如果上述条件全不满足。



n = 15      

def solution1(n):
    # 普通方法逐一判断添加元素
    dp = []
    for i in range(1,n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                dp.append('FizzBuzz')
            else:
                dp.append('Fizz')
        elif i % 5 == 0:
            dp.append('Buzz')
        else:
            dp.append(str(i))
            
    return dp



def solution2(n):
    # 初始化空值列表逐一添加元素，使用了0为假的技巧
    s = [''] * n
    for i in range(1, n + 1):
        if i % 3 and i % 5:  
            s[i-1] = str(i)
        if not i % 3:
            s[i-1] += 'Fizz'
        if not i % 5:
            s[i-1] += 'Buzz'
    return s



print(solution1(n))