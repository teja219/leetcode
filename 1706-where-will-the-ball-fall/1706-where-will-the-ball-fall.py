class Solution(object):
    def findBall(self, grid):
        countPrev = [[i] for i in range(len(grid[0]))]
        
        for row in grid:
            count = [[] for i in range(len(grid[0]))]
            for i in range(len(row)):
                if row[i]==-1:
                    if i-1>=0 and row[i-1]==-1:
                        for b in countPrev[i]:
                            count[i-1].append(b)
                if row[i]==1:
                    if i+1<len(grid[0]) and row[i+1]==1:
                        for b in countPrev[i]:
                            count[i+1].append(b)
            countPrev = count
                
        result = [-1 for i in range(len(grid[0]))]
        for j in range(len(count)):
            for b in count[j]:
                result[b]=j
        return result
                
        
        
        
        
        
        
        