class Solution(object):
    def maxProfit(self, prices, fee):
        dpHave = {}
        dpNotHave = {}
        
        prices.insert(0,-1)
        dpHave[1] = -prices[1]
        dpNotHave[1] = 0
        
        for i in range(2,len(prices)):
            dpHave[i] = max(dpHave[i-1],dpNotHave[i-1]-prices[i])
            dpNotHave[i] = max(dpNotHave[i-1],dpHave[i-1]+prices[i]-fee)
        
        return dpNotHave[len(prices)-1]
        