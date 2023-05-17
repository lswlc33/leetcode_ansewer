# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

test = [
    ["ab", "a"],
    ["dog","racecar","car"],
    ["flower","flow","flight"],
    [""],
    ["a"]
]


def longestCommonPrefix(strs):
    ans = "" # 初始化结果
    l = min(len(i) for i in strs) # 最短字符串长度
    
    for j in range(l+1): # 遍历下标
        x = 0 # 对比次数初始化
        for i in strs: # 遍历所有字符串
            if i[0:j] == strs[0][0:j]: # 与第一个对比
                x += 1 # 对比次数加1
            if x == len(strs): # 如果对比次数等于字符串的个数
                ans = i[0:j] # 更新结果
    return ans 



            




for i in test:
    print(longestCommonPrefix(i))