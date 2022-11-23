class Solution(object):
    def maximalSquare(self, matrix):
        dp = {}
        def recur(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==0 or j==0:
                if matrix[i][j]=="1":
                    return 1
                else:
                    return 0
            if matrix[i][j]=="0":
                dp[(i,j)] = 0
                return dp[(i,j)]
            
            dp[(i,j)] = min(recur(i-1,j),recur(i,j-1),recur(i-1,j-1))+1
            return dp[(i,j)]
        
        mx = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mx = max(recur(i,j),mx)
                # print (i,j,recur(i,j))
            
        
        # print(dp)
        return mx*mx
        
                    
            
            
                
        
        