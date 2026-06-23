class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 2
        counts = [0]*3
        for i in nums:
            counts[i] += 1
                
        index_sum = 0
        for i, count in enumerate(counts):
            counts[i] = index_sum
            index_sum += count
        
        sorted_lst = [0] * len(nums)
        for i in nums:
            sorted_lst[counts[i]] = i
            counts[i] += 1
        
        for i in range(len(nums)):
            nums[i] = sorted_lst[i]