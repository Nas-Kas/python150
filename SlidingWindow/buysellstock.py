'''
 [7,1,5,3,6,4]
  b
    s

[10,9,3,5,8,1,200] -> 199 b/c i can buy at 1 and sell at 199
            b
               s

if buy is greater than sell
reset* increment buy to sell
increment sell buy one
other wise increment
calc value set to a max
increase sell

max = 7
time 20 mins
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxVal = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                maxVal = max(maxVal, prices[sell] - prices[buy])
            sell += 1
        return maxVal