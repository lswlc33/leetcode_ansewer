
def reverse(x):
    x = str(x)

    if '-' in x:
        x = 0 - int(x[:0:-1])
    else:
        x = int(x[::-1])

    if -2147483648 < x < 2147483647:
        return x 
        
    return 0
