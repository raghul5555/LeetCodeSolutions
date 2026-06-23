class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        a_total = 0
        n = len(nums)
        for i in range(n):
            total += i+1
            a_total += nums[i]
        return total - a_total