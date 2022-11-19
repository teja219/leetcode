class Solution(object):
    def search(self, nums, target):
        
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                l = mid+1 #Note that we are always reducing the search space
            else:
                r = mid-1 #Note we are always reducing the search space
                
        return -1
        