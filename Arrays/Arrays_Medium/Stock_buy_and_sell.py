def stock_buy_and_sell_brute(prices):
    n=len(prices)
    maxProfit=0
    for i in range(n):
        for j in range(i+1,n):
            profit=prices[j]-prices[i]
            maxProfit=max(profit,maxProfit)
    return maxProfit
def stock_buy_and_sell_optimal(prices):
    minPrice=float('inf')
    maxProfit=0
    for price in prices:
        if price<minPrice:
            minPrice=price
        else:
            maxProfit=max(maxProfit,price-minPrice)
    return maxProfit
prices = [7, 1, 5, 3, 6, 4]
print(stock_buy_and_sell_brute(prices))
print(stock_buy_and_sell_optimal(prices))


