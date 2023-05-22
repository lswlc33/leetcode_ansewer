def isPalindrome(s):
    l = []

    for i in list(s):

        # 判断字母
        if i.isalnum():
            l.append(i.lower())

    if l == l[::-1]:
        return True

    return False


