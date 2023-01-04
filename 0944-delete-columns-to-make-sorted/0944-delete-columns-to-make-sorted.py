class Solution(object):
    def minDeletionSize(self, strs):
        total = 0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if ord(strs[j][i])<ord(strs[j-1][i]):
                    total += 1
                    break
        return total
        