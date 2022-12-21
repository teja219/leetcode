class Solution(object):
    def kthSmallest(self, matrix, k):
        alreadyVisited = {}
        alreadyVisited[(0,0)] = 1
        
        lis = [(matrix[0][0],0,0)]
        
        heapq.heapify(lis)

        count = 0
        result = 0
        while count < k:
            (ans,x,y) = heapq.heappop(lis)
            result = ans
            count += 1
            
            if x+1<len(matrix) and y<len(matrix) and (x+1,y) not in alreadyVisited:
                alreadyVisited[(x+1,y)]=1
                heapq.heappush(lis,(matrix[x+1][y],x+1,y))
                
            if x<len(matrix) and y+1<len(matrix) and (x,y+1) not in alreadyVisited:
                alreadyVisited[(x,y+1)]=1
                heapq.heappush(lis,(matrix[x][y+1],x,y+1))
        
        return result
            