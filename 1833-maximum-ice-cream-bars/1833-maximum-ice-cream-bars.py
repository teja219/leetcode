class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        
        total = coins
        bars = 0
        for c in costs:
            if coins-c>=0:
                coins -= c
                bars += 1
            else:
                break
        
        return bars
            
        
        
        