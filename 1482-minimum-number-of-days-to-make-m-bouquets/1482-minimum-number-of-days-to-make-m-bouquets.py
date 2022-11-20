class Solution(object):
    def minDays(self, bloomDay, m, k):
        
        def condition(D):
            bloomDayTemp = bloomDay[:]
            bloomDayTemp = [1 if x<=D else 0 for x in bloomDayTemp]
            # Find max consecutive days 
            # print(bloomDayTemp,D)
            i = 0 
            consecutiveDays = 0
            maxConsecutiveDays = 0
            totalBoq = 0
            while i<len(bloomDayTemp):
                if bloomDayTemp[i]==1:
                    consecutiveDays += 1
                else:
                    consecutiveDays = 0
                if consecutiveDays==k:
                   totalBoq += 1
                   consecutiveDays = 0
                i += 1
            return totalBoq>=m
        
        l = 0
        r = max(bloomDay)
        if len(bloomDay)<m*k:
            return -1
        while l<r:
            mid = (l+r)//2
            if condition(mid):
                r = mid
            else:
                l = mid+1
        return l