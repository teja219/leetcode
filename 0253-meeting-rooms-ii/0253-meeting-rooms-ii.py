class Solution(object):
    def minMeetingRooms(self, intervals):
        lis = []
        
        for x in intervals:
            lis.append((x[0],1))
            lis.append((x[1],0))
        
        lis.sort()
        
        
        maxOverlaps = 0
        currentOverlaps = 0
        for (t,f) in lis:
            if f==1:
                currentOverlaps += 1
            else:
                currentOverlaps -= 1
            
            if f==1:
                maxOverlaps = max(maxOverlaps,currentOverlaps)
        return maxOverlaps
        