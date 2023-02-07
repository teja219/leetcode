class Solution(object):
    def countBinarySubstrings(self, s):
        start = s[0]
        prevCount = 0
        count = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i]==start:
                count += 1
            else:
                start = s[i]
                ans += (min(count,prevCount))
                prevCount = count
                count = 1
            i += 1
        ans += (min(count,prevCount))
        return ans
        