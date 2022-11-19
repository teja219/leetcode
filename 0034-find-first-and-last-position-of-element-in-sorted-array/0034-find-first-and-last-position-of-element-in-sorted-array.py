class Solution(object):
        
    def searchRange(self, nums, target):
        
        def binaryFirstPosition(nums,target):
            start = 0
            end = len(nums)-1
            res = -1
            while start<=end:
                mid = (start+end)//2    
                if nums[mid]==target:
                    res = mid
                    end = mid-1
                elif nums[mid]<target:
                    start = mid+1
                else:
                    end = mid-1
            return res
    
        def binaryLastPosition(nums,target):
            start = 0
            end = len(nums)-1
            res = -1
            while start<=end:
                mid = (start+end)//2    
                if nums[mid]==target:
                    res = mid
                    start = mid+1
                elif nums[mid]<target:
                    start = mid+1
                else:
                    end = mid-1
            return res
    
        return [binaryFirstPosition(nums,target),binaryLastPosition(nums,target)]
        