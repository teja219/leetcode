class Solution(object):
    def findKthLargest(self, nums, k):
        
        lis = nums[:k]
        
        heapq.heapify(lis)
        
        for x in nums[k:]:
            heapq.heappush(lis,x)
            heapq.heappop(lis)
        return heapq.heappop(lis)
        
        
        