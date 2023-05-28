def isValid(s):
    s = list(s)
    tem = []
    dict = {
        ")":"(", 
        "]":"[", 
        "}":"{"
        }
        
    for i in s:
        if i in dict:
            if tem and tem[-1] == dict[i]:
                tem.pop()
            else:
                return False  
        else:
            tem.append(i)

    if tem:
        return False

    return True

print(isValid(s="()[]{}"))