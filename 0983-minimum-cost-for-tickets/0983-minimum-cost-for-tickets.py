class Solution(object):
    def mincostTickets(self, days, cost):
        dp = {}
        
        
        
        def recur(n):
            temp = n
            if temp in dp:
                return dp[n]
            
            if n>=len(days):
                return 0
            
            startDay = days[n]
            n = n + 1
            
            # print(cost[0],days[n:])
            minCost = cost[0] + recur(n)
            
            endDay = n
            while(endDay<=len(days)): 
                if endDay==len(days) or days[endDay] >= startDay + 7:
                    # print(cost[1],endDay,days[endDay:])
                    minCost = min(minCost,cost[1] + recur(endDay))
                    break
                endDay += 1
            
            endDay = n
            while(endDay<=len(days)): 
                if endDay==len(days) or days[endDay] >= startDay + 30:
                    # print(cost[2],endDay,days[endDay:])
                    minCost = min(minCost,cost[2] + recur(endDay))
                    break
                endDay += 1
            
            dp[temp] = minCost
            return minCost
                
            
        
        return recur(0)
        
            