class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] != nums[p1]:
                k+=1
                p1+=1
                nums[p1] = nums[p2]
        return k 