class Solution(object):
    def confusingNumber(self, n):
        mp = {}
        mp[1] = 1
        mp[6] = 9
        mp[9] = 6
        mp[8] = 8
        mp[0] = 0
    
        reverse = 0
        actual = n
        while n!=0:
            x = n%10
            if x not in mp:
                return False
            n = n//10
            reverse = reverse*10+mp[x]
        if reverse==actual:
            return False
        return True