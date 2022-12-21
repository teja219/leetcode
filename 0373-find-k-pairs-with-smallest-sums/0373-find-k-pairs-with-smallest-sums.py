class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        
        lis = [(nums1[0]+nums2[0],0,0)]
        
        heapq.heapify(lis)
        
        
        count = 0
        alreadyPushed = {}
        alreadyPushed[(0,0)] = 1
        results = []
        k = min(k,len(nums1)*len(nums2))
        while count<k:
            (ans,x,y) = heapq.heappop(lis)
            # print(count)
            results.append([nums1[x],nums2[y]])
            count += 1
            if x+1 < len(nums1) and y < len(nums2) and (x+1,y) not in alreadyPushed:
                alreadyPushed[(x+1,y)] = 1
                heapq.heappush(lis,(nums1[x+1]+nums2[y],x+1,y))
            if x < len(nums1) and y+1 < len(nums2) and (x,y+1) not in alreadyPushed:
                alreadyPushed[(x,y+1)] = 1
                heapq.heappush(lis,(nums1[x]+nums2[y+1],x,y+1))
        # print("----")
        return results    
                
        
        
        