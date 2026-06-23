class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = [i**2 for i in nums]
        s.sort()
        return s