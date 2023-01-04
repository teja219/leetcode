class Solution(object):
    def findBall(self, grid):
        R = len(grid)-1
        
        def singleRow(rowDp,C):
            results = []
            for i in range(0,C):
                if rowDp[i]==1:
                    if rowDp[i+1]==1:
                        results.append(1)
                    else:
                        results.append(0)
                if rowDp[i]==-1:
                    if rowDp[i-1]==-1:
                        results.append(1)
                    else:
                        results.append(0)
            return results
    
        def convertRowToDp(row):
            dp = {}
            for i in range(len(row)):
                dp[i] = row[i]
            dp[-1] = 1
            dp[len(row)] = -1
            return dp
        
        def recur(grid,r):
            if r==0:
                dp = convertRowToDp(grid[r])
                return [singleRow(dp,len(grid[0]))]
            result1 = recur(grid,r-1)
            result2 = singleRow(convertRowToDp(grid[r]),len(grid[0]))
            result1.append(result2)
            return result1
            
        result = recur(grid,len(grid)-1)
        countPrev = [[i] for i in range(len(grid[0]))]
        
        # print(result)
        for i in range(len(result)):
            count = [[] for j in range(len(grid[0]))]
            for j in range(len(grid[i])):
                if result[i][j]==1:
                    if grid[i][j]==1:
                        for b in countPrev[j]:
                            count[j+1].append(b)
                    else:
                        for b in countPrev[j]:
                            count[j-1].append(b)
            countPrev = count
        
        
        result = [-1 for i in range(len(grid[0]))]
        
        for c in range(len(count)):
            for b in count[c]:
                result[b]=c
        return result
                
        
        
        
        
        
        
        