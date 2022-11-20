class Solution(object):
    def mySqrt(self, x):
        def condition(r):
            return r*r>=x
        
        l = 0
        r = x
        
        while l<r:
            # print(l,r)
            mid = (l+r)//2
            if condition(mid):
                r = mid
            else:
                l = mid+1
        
        if l*l == x:
            return l
        else:
            return l-1
        