class Solution(object):
    def findTheLongestSubstring(self, s):
        
        oddMin = -1
        
        pos = {}
        pos['a'] = 0
        pos['e'] = 1
        pos['i'] = 2
        pos['o'] = 3
        pos['u'] = 4
        
        currentState = "11111"
        previousStates = {}
        
        previousStates[currentState] = -1
        
        maxLen = 0
        for i in range(len(s)):
            x = s[i]
            if x in pos:
                if currentState[pos[x]]=='1':
                    currentState = currentState[:pos[x]]+'0'+currentState[pos[x]+1:]
                else:
                    currentState = currentState[:pos[x]]+'1'+currentState[pos[x]+1:]
            
            if currentState in previousStates:
                maxLen = max(maxLen,i-previousStates[currentState])
            else:
                previousStates[currentState] = i
        
        return maxLen
            
        