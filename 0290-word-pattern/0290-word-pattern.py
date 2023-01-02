class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        mp = {}
        mp1 = {}
        if len(pattern)!=len(words):
            return False
        
        for i in range(len(words)):
            if pattern[i] in mp:
                if mp[pattern[i]] != words[i]:
                    return False
            elif words[i] in mp1:
                if mp1[words[i]] != pattern[i]:
                    return False
            else:
                mp[pattern[i]] = words[i]
                mp1[words[i]] = pattern[i]
        return True
            
        