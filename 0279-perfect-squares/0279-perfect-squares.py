class Solution(object):
    
    
    def numSquares(self, n):
        dp2 = {}
        x = 1
        perfectSquares = []
        while x*x <= 10001:
            dp2[x*x] = True
            perfectSquares.append(x*x)
            x = x +1
        
        perfectSquares.reverse()
        dp = {}
        
        def recur(n):
            
            if n in dp:
                return dp[n]
            
            if n in dp2:
                dp[n] = 1
                return 1
            minAns = 10000000000000
            for x in perfectSquares:
                if n-x>0:
                    minAns = min(minAns,1+recur(n-x))
            dp[n] = minAns
            return dp[n]
        
        return recur(n)
        