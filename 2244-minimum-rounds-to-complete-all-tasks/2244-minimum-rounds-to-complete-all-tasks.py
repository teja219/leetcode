class Solution(object):
    def minimumRounds(self, tasks):
        dp = {}
        def rounds(T):
            if T in dp:
                return dp[T]
            if T==1:
                return -1
            if T==2 or T==3:
                return 1
            if T==4:
                return 2
            dp[T] = min(rounds(T-2),rounds(T-3))+1
            return dp[T]
            
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
                # print("Entered")
                total += rounds(v)
        return int(total)
                
        