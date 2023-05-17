# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

s = ["h","e","l","l","o"]

# 调包法
def reverseString1(s):
    return s.reverse()

# 双指针法（伪）
def reverseString2(s):
    b = len(s) - 1

    for a in range(len(s)//2):
        s[a], s[b] = s[b], s[a]
        b -= 1

    return s

# 双指针法（真）
def reverseString6(s):
    a, b = 0, len(s) - 1

    while b > len(s) // 2:
        temp = s[a]
        s[a] = s[b]
        s[b] = temp

        a += 1
        b -= 1

    return s

# 替身遍历替换法
def reverseString3(s):

    r = [""] * len(s)

    for i in range(0, len(s)):
        r[-i -1] = s[i]
        
    return r


# 列表表达式法
def reverseString4(s):
    return [s[i] for i in range(len(s)-1, -1, -1)]

# 反着切片法
def reverseString5(s):
    return s[::-1]

print(reverseString6(s))