class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)>2:
            nums = list(set(nums))
            if len(nums)>2:
                nums.sort(reverse=True)            
                return nums[2]
            else:
                return max(nums)
        else:
            return max(nums)