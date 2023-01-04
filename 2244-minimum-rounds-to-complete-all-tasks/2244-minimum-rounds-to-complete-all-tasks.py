class Solution(object):
    def minimumRounds(self, tasks):
        dp = {}
        def rounds(T):
            if T==1:
                return -1
            if T%3==0:
                return T/3
            if T%3==2:
                return (T/3)+1
            if T%3==1:
                return (T/3)+1
            
        mp = {}
        for x in tasks:
            if x in mp:
                mp[x]+=1
            else:
                mp[x]=1
        total = 0
        
        for (k,v) in mp.items():
            if v == 1:
                return -1
            else:
                total += rounds(v)
        return int(total)
                
        