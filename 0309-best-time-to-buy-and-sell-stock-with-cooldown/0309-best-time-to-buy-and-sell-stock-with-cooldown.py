class Solution(object):
    def maxProfit(self, prices):
        
        prices.insert(0,-1)
        dpHave = {}
        dpNotHave = {}
        
        dpHave[1] = - prices[1]
        dpNotHave[1] = 0
        dpNotHave[0] = 0
        for i in range(2,len(prices)):
            dpHave[i] = max(dpHave[i-1],dpNotHave[i-2]-prices[i])
            dpNotHave[i] = max(dpNotHave[i-1],dpHave[i-1]+prices[i])
        
        return max(dpHave[len(prices)-1],dpNotHave[len(prices)-1])
        