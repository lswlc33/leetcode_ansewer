def isAnagram1(s, t):
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    dict2 = {}
    for i in t:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1

    if dict1 == dict2:
        return True
    return False

def isAnagram2(s, t):
    s = sorted(list(s))
    t = sorted(list(t))

    if s == t:
        return True
    return False