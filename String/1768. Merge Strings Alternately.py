class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        res = ""
        l1 = len(word1)
        l2 = len(word2)
        while i<l1 and j<l2:
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        while i<l1:
            res+=word1[i]
            i+=1
        while j<l2:
            res+=word2[j]
            j+=1
        return res