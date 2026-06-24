class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k>len(nums):
            return 0
        max_sum = 0
        r_sum = 0
        freq = {}
        for i in range(len(nums)-k+1):
            if i==0:
                for j in range(k):
                    freq[nums[j]] = freq.get(nums[j], 0)+1
                    r_sum+=nums[j]
            else:
                freq[nums[i-1]] -= 1
                if freq[nums[i-1]]==0:
                    del freq[nums[i-1]]
                freq[nums[i+k-1]] = freq.get(nums[i+k-1], 0) + 1
                r_sum-=nums[i-1]
                r_sum+=nums[i+k-1]

            if len(freq)==k:
                max_sum = max(max_sum, r_sum)

        return max_sum