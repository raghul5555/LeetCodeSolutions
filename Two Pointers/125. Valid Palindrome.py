class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ""
        for i in s:
            if i.isalnum():
                a+=i.lower()
        i = 0
        j = len(a)-1
        while i<j:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True