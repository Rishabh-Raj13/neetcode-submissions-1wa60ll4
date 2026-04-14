class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        # for low in range(len(prices)-1):
        #     for high in range(low+1,len(prices)):
        #         if prices[low] < prices[high]:
        #             maxProfit = max(maxProfit,prices[high]-prices[low])
        #         else:
        #             pass
        # return maxProfit
        minPrice = float('inf')
        for price in prices:
            minPrice=min(minPrice,price)
            maxProfit = max(maxProfit,price-minPrice)

        return maxProfit


        