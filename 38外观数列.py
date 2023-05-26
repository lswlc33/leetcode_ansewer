def countAndSay(n):
    m = "1"
    for i in range(n - 1):
        x = 0
        cur_n = ""
        times = 1
        tem = ""
        while x < len(m):
            if m[x] == cur_n:
                times += 1
            else:
                if x != 0:
                    tem += str(times) + cur_n
                cur_n = m[x]
                times = 1

            if x == len(m) - 1:
                tem += str(times) + cur_n

            x += 1

        m = tem

    return m


print(countAndSay(n=5))
