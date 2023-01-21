class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        
        base = n
        
        def convertLastNonZeroAndAddOne(n):
            base = n
            count = 0
            while n%10==0:
                n=n/10
                count += 1
            extra = pow(10,count)
            return base+extra
                
        while 1:
            if sum([int(c) for c in str(n)])<=target:
                return n-base
            n = convertLastNonZeroAndAddOne(n)
                
        
        
        
        return 0
        