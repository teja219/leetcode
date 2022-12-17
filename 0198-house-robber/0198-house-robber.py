class Solution(object):
    def rob(self, nums):
        dp = {}
        def recur(n):
            if n in dp:
                return dp[n]
            if n==0:
                return nums[0]
            if n==1:
                return max(nums[0],nums[1])
            
            dp[n] = max(recur(n-2)+nums[n],recur(n-1))
            return dp[n]
        
        return recur(len(nums)-1)
        