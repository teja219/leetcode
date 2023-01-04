class Solution(object):
    def isHappy(self, n):
        prev = 0
        mp = {}
        mp[n]=1
        
        while 1:
            temp = 0
            for i in str(n):
                temp += (int(i)*int(i))
            n = temp
            if n==1:
                return True
            if n in mp:
               return False
            else:
               mp[n] = 1
        
        
        return False
        