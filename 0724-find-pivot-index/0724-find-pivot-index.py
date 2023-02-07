class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == (total-left-nums[i]):
                return i
            else:
                left += nums[i]
        return -1
            
        