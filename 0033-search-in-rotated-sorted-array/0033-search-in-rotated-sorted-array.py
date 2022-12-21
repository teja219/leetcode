class Solution(object):
    def search(self, nums, target):
        
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[0]:
                right = mid
            else:
                left = mid+1
        
        pivot = left
        right = len(nums)-1
        # print(pivot)
        if nums[pivot]<=target and target<=nums[right]:
            left = pivot
            while left<right:
                mid = (left+right)//2
                if nums[mid]>=target:
                    right = mid
                else:
                    left = mid+1
            if nums[left]==target:
                return left
            else:
                return -1
        elif pivot!=0 and nums[0]<=target and nums[pivot-1]>=target:
            left = 0
            right = pivot-1
            while left<right:
                mid = (left+right)//2
                if nums[mid]>=target:
                    right = mid
                else:
                    left = mid+1
            if nums[left]==target:
                return left
            else:
                return -1
        else:
            return -1
            
        
        