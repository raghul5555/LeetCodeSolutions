class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = [i for i in s]
        i = 0
        j = len(t)-1
        while i<j:
            if t[i].isalpha() and t[j].isalpha():
                t[i], t[j] = t[j], t[i]
                i+=1
                j-=1
            elif not t[i].isalpha():
                i+=1
            elif not t[j].isalpha():
                j-=1
            else:
                i+=1
                j-=1
        return "".join(t)