# 给你一个字符串 s，找到 s 中最长的回文子串。
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。




def longestPalindrome(s):
    # 可行但是复杂度颇高
    ans = ""
    def isaba(text):
        # 如果字符串正反相等就是回文
        return text == text[::-1]
    
    # isaba()的复杂方法实现
    # def isaba(text):
    #     for i in range((len(text)-1)):
    #         if text[i] == text[len(text) - 1 - i]:
    #             # 依次判断左边的数字是否等于右边的
    #             pass
    #         else:
    #             return False
    #     return True
    
    for i in range(len(s)):
        for j in range(i + 1,len(s) + 1):
            # 遍历所有可能的字符串
            temp = s[i:j]
            if isaba(temp) and len(ans) < len(temp):
                # 如果是回文且他比已有的要长就更新
                ans = temp
    return ans

def longestPalindrome1(s):
    ans = ""

    # 只有一个字符是回文
    if len(s) == 1:   
        return s
    
    for i in range(len(s)): # 遍历字符串

        # 一、奇数长度的回文串
        a = isaba = 1   # a是步长iasba是个bool
        while isaba:
            if i - a >= 0 and i + a <= len(s) - 1 and s[i - a] == s[i + a]:   
                if len(ans) < 2*a + 1:  # 更新答案
                    ans = s[i - a:i + a + 1]
                a += 1
            else:
                isaba = 0
         
        # 二、偶数长度的回文串
        a = isaba = 1
        while isaba:
            if i - a >= 0 and i + a <= len(s) and s[i - a] == s[i+a-1]: 
                if len(ans) < 2*a:
                    ans = s[i-a:i+a]
                a += 1
            else:
                isaba = 0

    # 上面找不到，返回个单字
    if ans == "":   
        return s[0]
    
    # 返回答案
    return ans



