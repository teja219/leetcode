class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = {}
        def recur(i,m,n):
            if (i,m,n) in dp:
                return dp[(i,m,n)]
            if (i,m,n) in dp:
                return dp[(i,m,n)]
            if m<0 or n<0:
                return -1000000000000000000
            ones = strs[i].count("1")
            zeroes = strs[i].count("0")
            if i==0:
                if m>=zeroes and n>=ones:
                    return 1
                else:
                    return 0
            
            dp[(i,m,n)] = max(recur(i-1,m-zeroes,n-ones)+1,recur(i-1,m,n))
            return dp[(i,m,n)]
        z = recur(len(strs)-1,m,n)
        if z<=-1:
            return 0
        else:
            return z
            