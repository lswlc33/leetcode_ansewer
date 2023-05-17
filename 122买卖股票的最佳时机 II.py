prices = [7,1,5,3,6,4]

# 贪心算法
def maxProfit1(prices):
    a = 1
    b = sum = 0
    

    while a != len(prices):
        if prices[a] > prices[b]:
            sum += prices[a] - prices[b]
        b += 1
        a += 1

    return sum

# 提取数组中最大连续升序字串法
def maxProfit1(prices):
    
    a = b = sum = 0
    
    while a != len(prices):
            
        if a - 1 >= 0 and prices[a] <= prices[a - 1]:
            sum += prices[a - 1] - prices[b]
            b = a
        
        if a + 1== len(prices):
            sum += prices[a] - prices[b]

        a += 1

    return sum
