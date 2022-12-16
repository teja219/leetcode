class Solution(object):
    
    
    def climbStairs(self,n):
        dp = {}
        def recur(n):
            if n in dp:
                return dp[n]
            if n==0:
                return 1
            elif n==1:
                return 1
            else:
                dp[n] = recur(n-1)+recur(n-2)
                return dp[n]
        return recur(n)
        