class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def isPal(s):
            i=0
            j=len(s)-1
            pal =True
            while i<j:
                if s[i]!=s[j]:
                    pal=False
                    break
                i+=1
                j-=1
            return pal
        for word in words:
            if isPal(word):
                return word
        return ""