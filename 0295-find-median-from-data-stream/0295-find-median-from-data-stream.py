class MedianFinder(object):

    def __init__(self):
        self.heapLeft = [10000000000]
        self.heapRight = [10000000000]
        
        heapq.heapify(self.heapLeft)
        heapq.heapify(self.heapRight)
    
    def addNum(self, num):
        leftSize = len(self.heapLeft)
        rightSize = len(self.heapRight)
    
            
        leftTop = -heapq.heappop(self.heapLeft)
        rightTop = heapq.heappop(self.heapRight)
        
        heapq.heappush(self.heapLeft,-min(leftTop,rightTop,num))
        heapq.heappush(self.heapRight,max(leftTop,rightTop,num))
        
        pivot = leftTop + rightTop + num - min(leftTop,rightTop,num) - max(leftTop,rightTop,num)
        
        if rightSize<=leftSize:
            heapq.heappush(self.heapRight,pivot)
        else:
            heapq.heappush(self.heapLeft,-pivot)
            
    def findMedian(self):
        
        leftSize = len(self.heapLeft)
        rightSize = len(self.heapRight)
        # print(self.heapLeft)
        # print(self.heapRight)
        
        leftTop = -self.heapLeft[0]
        rightTop = self.heapRight[0]
        
        # print("%%%%")
        if leftSize == rightSize:
            return (leftTop+rightTop)/2.0
        elif leftSize < rightSize:
            return rightTop
        else:
            return leftTop
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()