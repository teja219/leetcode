class Solution(object):
    def removeDuplicates(self, s, k):
        
        st = deque([])
        
        for i in range(len(s)):
            if i==0 or len(st)==0 or s[i]!=st[-1][0]:
                st.append((s[i],1))
            else:
                if st[-1][0]==s[i]:
                    # print(st[-1])
                    st[-1] = (st[-1][0],(st[-1][1] + 1)%k)
                    if st[-1][1]==0:
                        st.pop()
        # print(st)
        
        result = ""
        for i in range(len(st)):
            for j in range(st[i][1]):
                result += st[i][0]
        return result
        
            
        
        