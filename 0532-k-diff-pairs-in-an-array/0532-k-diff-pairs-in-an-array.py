class Solution(object):
    def findPairs(self, nums, k):
        if k==0:
            nums.sort()
            mp = {}
            for x in nums:
                if x in mp:
                    mp[x]+=1
                else:
                    mp[x]=1
            total = 0
            for (x,y) in mp.items():
                if y>1:
                    total += 1
            return total
        nums = list(set(nums))
        print(nums)
        mp = {}
        count = 0
        for i in range(len(nums)):
            if (nums[i]-k) in mp:
                print(i,nums[i],nums[i]-k)
                count += mp[nums[i]-k]
            if (nums[i]+k) in mp:
                count += mp[nums[i]+k]
                print(i,nums[i],nums[i]+k)
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
        return count
            
        