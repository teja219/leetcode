class Solution(object):
    def shipWithinDays(self, weights, days):
        
        def condition(W):
            d = 0
            if(max(weights)>W):
                return False
            
            i = 0
            S = 0
            d = 0
            while i < len(weights):
                S += weights[i]
                # print(S,i)
                if S>W:
                    d += 1
                    S = weights[i]
                i += 1
            if S != 0:
                d += 1
            # print "#",(W,d)
            return d<=days
        
        
        l = 0
        r = sum(weights)
        # print(condition(15))
        while l<r:
            mid = (l+r)//2
            # print(l,mid,r)
            if condition(mid):
                r = mid
            else:
                l = mid+1
            
        return l