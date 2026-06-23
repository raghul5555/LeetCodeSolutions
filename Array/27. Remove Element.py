class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        li = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val :
                nums[i], nums[li] = nums[li], nums[i]
                li -= 1
        return li+1