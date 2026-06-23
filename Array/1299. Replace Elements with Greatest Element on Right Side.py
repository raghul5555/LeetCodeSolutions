class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        m = -1 
        for i in range(len(arr)-1, -1, -1):
            arr[i], m = m, max(m, arr[i])
        return arr