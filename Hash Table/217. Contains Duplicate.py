class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = set()
        for i in nums:
            if i in temp:
                return True
            temp.add(i)
        return False