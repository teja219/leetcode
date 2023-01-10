class Solution(object):
    def longestCommonPrefix(self, strs):
        minL = 100000000000
        for str_ in strs:
            minL = min(minL,len(str_))
        
        count = 0
        for j in range(minL):
            for i in range(1,len(strs)):
                if strs[i][j]!=strs[i-1][j]:
                    return strs[i][:count]
            count += 1
        
        return strs[0][:count]
                
        