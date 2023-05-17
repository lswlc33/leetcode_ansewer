# 给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i​​​​​​​​​​​​ 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。
# 客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。


accounts = [[1,5],[7,3],[3,5]]


def solution1(accounts):
    # 最基本的方法
    list = []
    for i in accounts:
        m = 0
        for j in i:
            m = m + j
        list.append(m)
        
    n = list[0]
    for i in range(1,len(list)):
        if list[i] > n:
            n = list[i]
    return n

def solution2(accounts):
    # 使用sum和max函数代替手动算
    list = []
    for i in accounts:
        list.append(sum(i))
    return max(list)

def solution3(accounts):
        #把for循环写在一行里
        return max(sum(i) for i in accounts)


def solution4(accounts):
        # 使用map函数代替for循环
        return max(map(sum,accounts))


# map的介绍
# map() 是一种内置的高阶函数，它把一个函数应用到一个可迭代的对象（如列表、元组或集合）的每个元素上，并返回一个新的可迭代对象，其中包含应用函数后的结果。
# map(fun, data) fun: 要执行的函数  data:要处理的数据



print(solution1(accounts))