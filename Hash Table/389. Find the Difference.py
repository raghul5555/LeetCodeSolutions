class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t1 = sum(ord(i) for i in s)
        t2 = sum(ord(i) for i in t)
        return chr(t2-t1)