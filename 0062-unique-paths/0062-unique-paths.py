class Solution(object):
    def uniquePaths(self, m, n):
        
        dp = {}
        def recur(m,n):
            if (m,n) in dp:
                return dp[(m,n)]
            if m==0 or n==0:
                return 1
            dp[(m,n)] = recur(m-1,n)+recur(m,n-1)
            return dp[(m,n)]
        
        return recur(m-1,n-1)