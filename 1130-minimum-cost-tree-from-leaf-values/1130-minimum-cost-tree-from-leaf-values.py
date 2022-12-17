class Solution(object):
    def mctFromLeafValues(self, arr):
        dp = {}
        def recur(i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            if i==j:
                dp[(i,j)] = (0,arr[i])
                return dp[(i,j)]
            if j==i+1:
                dp[(i,j)] = (arr[i]*arr[j],max(arr[i],arr[j]))
                return dp[(i,j)]
            # prod = 1
            # for k in range(i,j+1):
            #     product *= arr[k]
                
            ans = 10000000000
            maxX = 0
            for k in range(i,j):
                (lProduct,lMax) = recur(i,k)
                (rProduct,rMax) = recur(k+1,j)
                ans = min(ans,lProduct+rProduct+lMax*rMax)
                maxX = max(maxX,lMax,rMax)
            
            dp[(i,j)] = (ans,maxX)
            return (ans,maxX)
        
        x = recur(0,len(arr)-1)
        # print(dp)
        return x[0]