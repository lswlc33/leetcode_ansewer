def myAtoi(s):

    s = list(s)
    is_below_0 = False
    r = ""

    for i in range(len(s)):
        if s[i] != " ":
            s = s[i:]
            break


    for i in range(len(s)):
        if s[i] == "+":
            s = s[i + 1:]
        elif s[i] == "-":
            s = s[i + 1:]
            is_below_0 = True
        break
        

    for i in range(len(s)):
        if not s[i].isdigit():
            s = s[:i]
            break


    if s ==[]:
        return 0
    elif is_below_0:
        s.insert(0,"-")

    return max(min(int("".join(s)) ,2147483647) ,-2147483648)