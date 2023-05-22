# 哈希表
def firstUniqChar1(self, s: str) -> int:
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in dict:
        if dict[i] == 1:
            return s.index(i)
    return -1


# 简单计数
def firstUniqChar2(self, s: str) -> int:
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1