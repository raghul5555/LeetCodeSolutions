class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums)-1:
                    if count > max_ones:
                        max_ones = count
            elif count != 0:
                if count > max_ones:
                    max_ones = count
                count = 0
        return max_ones