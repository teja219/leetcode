class Solution(object):
    def findMin(self, nums):
        if nums[0]<nums[-1]:
            return nums[0]
        def cond(x):
            return x<nums[0]
        
        left = 0
        right = len(nums)-1
        
        while left<right:
            
            mid = (left+right)//2
            # print(left,mid,right)
            if cond(nums[mid]):
                right = mid
            else:
                left = mid+1
                
        return nums[left]
        