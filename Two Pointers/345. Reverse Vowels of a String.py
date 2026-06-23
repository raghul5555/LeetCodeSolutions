class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1
        t = [ch for ch in s]
        vowels = "aeiou"
        while i<j:
            if t[i].lower() in vowels and t[j].lower() in vowels:
                t[i], t[j] = t[j], t[i]
                i+=1
                j-=1
            elif t[i].lower() not in vowels:
                i+=1
            elif t[j].lower() not in vowels:
                j-=1
            else:
                i+=1
                j-=1
        return "".join(t)