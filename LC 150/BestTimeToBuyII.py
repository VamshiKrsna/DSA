# LC 150 : Best Time To Buy & Sell Stock II
def maxProf(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

if __name__ == '__main__':
    # prices = [1,2,3,4,5]
    # prices = [7,6,4,3,1]
    # Auxiliary Space O(1) :
    prices = [7,1,5,3,6,4]
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    print(profit)

    # Container & Summation :
    gains = []
    for i in range(len(prices)-1):
        if prices[i] < prices[i + 1]:
            gains.append(prices[i + 1] - prices[i])
    print(sum(gains))

    # DP :
    import math
    HOLD, KEEPCASH = 0,1
    dp = dict()
    dp[-1,HOLD] = -math.inf
    dp[-1,KEEPCASH] = 0
    for day, price in enumerate(prices):
        dp[day,HOLD] = max(dp[day-1,HOLD],dp[day-1,KEEPCASH] - price)
        dp[day,KEEPCASH] = max(dp[day-1,KEEPCASH], dp[day-1,HOLD] + price)
    last_day = len(prices)-1
    print(dp[last_day,KEEPCASH])
    print(maxProf(prices))
