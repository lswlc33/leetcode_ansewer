haystack = "mississippi"

needle = "issip"

def strStr(haystack, needle):
    x, y= len(haystack), len(needle)
    a, b = 0, 0
    while x != a and y != b:
        if haystack[a] == needle[b]:
            a += 1
            b += 1
        else:
            a = a - b + 1
            b = 0
        if b == y:
            return a - b
    return -1

def strStr1(haystack, needle):
    x = len(haystack)
    y = len(needle)
    for i in range(x):
        if haystack[i:i+y] == needle:
            return i
    return -1 

def strStr2(haystack, needle):
    return haystack.find(needle)
  

strStr2(haystack, needle)