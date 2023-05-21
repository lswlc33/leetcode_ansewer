def minLength1(s):

    while "AB" in s or "CD" in s:

        # s = s.replace("AB","")
        # s = s.replace("CD","")   
        # 合并成下面
        s = s.replace("AB","").replace("CD","")

    return len(s)


def minLength2(s):

    # 栈
    tem = []

    for i in s:
        # 匹配成功就弹出
        if tem and tem[-1] == 'A' and i =="B":
            tem.pop()
        elif tem and tem[-1] == 'C' and i =="D":
            tem.pop()
        # 匹配失败就加入   
        else:              
            tem.append(i)

    s = ''

    return len(tem)
