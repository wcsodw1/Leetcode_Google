# python Q121_Buy_and_Sell_Stock.py


class Solution:
    def maxProfit(self, prices):

        # 1.Set basic parameter
        previous, order = 0, 1
        maxProfit = 0

        # 2.這邊 while 是來設定迴圈等於股價資料改變的資料長度( len(price)-1 )
        while order < len(prices):

            # 3.record the "order data value"
            # 3.1 if "order data(order)"" bigger then previous, save it
            if prices[previous] < prices[order]:
                profit = prices[order] - prices[previous]
                #print("maxProfit : ", maxProfit)
                #print("profit :　", profit)
                maxProfit = max(maxProfit, profit)

            # 3.2 or update the previous(if order data lower then previous)
            else:
                previous = order
            #print("Previous : ", previous)
            order += 1
            #print("order ", order)

        print("Latest maxProfit : ", maxProfit)

        return maxProfit


prices = [7, 1, 3, 6, 2, 3, 0.5, 7]
obj = Solution()
print(obj.maxProfit(prices))
