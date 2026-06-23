from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        decreases = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                decreases += 1
                if decreases > 1:
                    return False
        return True