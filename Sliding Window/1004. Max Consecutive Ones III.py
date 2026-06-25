class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_c = 0
        l = 0
        r = 0
        c = 0
        n = len(nums)
        while l<=r and r<n:
            if nums[r]==0:
                c+=1
            while c>k:
                if nums[l]==0:
                    c-=1
                l+=1
            max_c = max(max_c, r-l+1)
            r+=1
        
        return max_c