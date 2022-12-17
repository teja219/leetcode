class Solution(object):
    def numTrees(self, n):
        
        dp = {}
        def recur(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j<i:
                return 1
            if i==j:
                dp[(i,j)] = 1
                return 1
            if i+1==j:
                dp[(i,j)] = 2
                return 2
            
            k = i
            total = 0
            for k in range(i,j+1):
                zz1 = recur(i,k-1)
                zz2 = recur(k+1,j)
                # print("###",k)
                # if i==1 and j==3:
                #     print(i,k-1,zz1)
                #     print(k+1,j,zz2)
                total += (zz1*zz2)
            
            dp[(i,j)] = total
            return total
        
        z = recur(1,n)
        # print(dp)
        return z