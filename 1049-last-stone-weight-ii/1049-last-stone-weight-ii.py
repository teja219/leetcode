class Solution(object):
    def lastStoneWeightII(self, stones):
        dp = {}
        def recur(totalWeight,n):
            if (totalWeight,n) in dp:
                return dp[(totalWeight,n)]
            if totalWeight == 0:
                dp[(totalWeight,n)] = True
                return True
            if n==0:
                dp[(totalWeight,n)] = False
                return False
            
            if stones[n]>totalWeight:
                dp[(totalWeight,n)] = recur(totalWeight,n-1)
            else:
                dp[(totalWeight,n)] = ( recur(totalWeight,n-1) or recur(totalWeight-stones[n],n-1) )
        
            return dp[(totalWeight,n)]
        
        totalWeight = sum(stones)
        ans = totalWeight
        for w in range(1,totalWeight+1):
            if recur(w,len(stones)-1):
                ans = min(ans,abs(2*w-totalWeight))
        return ans
            
        
    
    
    
    
        