class Solution(object):
    def numRollsToTarget(self, n, k, target):
        
        dp = {}
        def recur(n,target):
            if (n,target) in dp:
                return dp[(n,target)]
            if n==0 and target==0:
                return 1
            if target<0:
                return 0
            if n==0:
                return 0
            total = 0
            for i in range(1,k+1):
                total += recur(n-1,target-i)
                total = total % 1000000007
            
            dp[(n,target)] = total
            return total % 1000000007
        
        return recur(n,target)%1000000007
        
        