def maxProfit(prices):
        res = prices[0]
        max_profit = 0
        for num in prices:
            res = min(res, num)
            price = num - res
            max_profit = max(max_profit, price)
        return max_profit
prices = [7,6,4,3,1]
print(maxProfit(prices))