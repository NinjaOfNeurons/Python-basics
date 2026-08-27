class Solution:
    def stocks(self, days_price : list)-> tuple:
        max_profit = 0
        min_price = days_price[0]
        #condition is first i have to buy at min price then going forward to sell it at max price in a single pass.
        for price in days_price:
            
            if min_price > price:
                min_price = price

            today_profit  = price - min_price   # this thing is important 

            if max_profit < today_profit:
                max_profit = today_profit
        return(min_price, max_profit)






obj = Solution()
print(obj.stocks([7, 1, 5, 3, 6, 4]))