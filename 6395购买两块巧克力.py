
def buyChoco(prices, money):
    prices = sorted(prices)
    if prices[0] + prices[1] <= money:
        return money - prices[0] - prices[1]
    return money