class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        if s=="":
            return True
        while t and i<len(t):
            if t[i]==s[j]:
                i+=1
                j+=1
                if j==len(s):
                    return True
                continue
            i+=1
        return False