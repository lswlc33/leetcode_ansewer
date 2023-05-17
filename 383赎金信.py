# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 如果可以，返回 true ；否则返回 false 。
# magazine 中的每个字符只能在 ransomNote 中使用一次。

ransomNote = "aa"
magazine = "aab"

# 构造列表逐字验证
def canConstruct1(ransomNote: str, magazine: str):
    r = []
    for i in magazine:
        r.append(i) 
    for i in ransomNote:
        if i in r:
            r.remove(i)
        else:
            return False
    return True
    

# 获取元素种类，对比元素数量
def canConstruct2(ransomNote: str, magazine: str):
    r = set(ransomNote)
    for i in r:
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True
