# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

s = "a good   example"



def reverseWords(s):

    # 把字符串按照空格转成列表
    list1 = []
    word_start = -1
    word_end = 0
    for i in range(len(s)):
        if s[i] == " ":
            word_end = i
            list1.append(s[word_start +1:word_end])
            word_start = word_end
    list1.append(s[word_start+1:])

    # 删除多余的空格
    while "" in list1:
        list1.remove("")

    # 反转列表
    # 由于range里是从大到小，直接返回是空的，所以在步长设置-1方可正常遍历
    list2 = []
    for i in range(-1,-1 - len(list1),-1):
        list2.append(list1[i])
    
    # 把列表转成字符串
    answer_string = ""
    for i in range(len(list2)):
        answer_string += list2[i] 
        if i < len(list2):
            answer_string += " "

    # 返回答案
    return answer_string

def reverseWords2(s):
    s = s.split()   # 分割单词
    s = s[::-1]     # 倒叙列表
    s = " ".join(s) # 加入空格转为字符串
    return s        # 输出答案

def reverseWords3(s):
    return " ".join(s.split()[::-1])

def reverseWords4(s):
    s = s[::-1]             # 倒叙字符串
    s = s.split()           # 分割字符串
    for i in range(len(s)): # 翻转列表的每个元素
        s[i] = s[i][::-1]
    s = " ".join(s)         # 加入空格转为字符串
    return s

print(reverseWords4(s))