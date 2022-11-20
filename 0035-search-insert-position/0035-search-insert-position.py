class Solution(object):
    def searchInsert(self, nums, target):
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        def condition(x):
            return x>=target
        
        l = 0
        r = len(nums)-1
        
        while l<r:
            mid = (l+r)//2
            
            if condition(nums[mid]):
                r = mid
            else:
                l = mid+1
        print(l)
        return l
            
        
        