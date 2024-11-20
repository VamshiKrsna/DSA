# LC 150 : Best Time to buy and sell stock
def profit(prices):
    buy = prices[0]
    prof = 0
    for i in range(1,len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > prof:
            prof = prices[i] - buy
    return prof

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    buy = prices[0]
    prof = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > prof:
            prof = prices[i]-buy
    print(prof)
    print(profit(prices))