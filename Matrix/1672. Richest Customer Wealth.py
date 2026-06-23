class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=0
        for i in accounts:
            k=sum(i)
            if k>m:
                m=k
        return m