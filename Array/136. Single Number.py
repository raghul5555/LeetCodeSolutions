class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
        for i in range(len(nums)):
            if freq_map[nums[i]]==1:
                return nums[i]