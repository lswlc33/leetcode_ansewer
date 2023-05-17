
def countSeniors(details):
    num = 0
    for i in range(len(details)):
        if int(details[i][-4:-2]) > 60:
            num += 1
    return num