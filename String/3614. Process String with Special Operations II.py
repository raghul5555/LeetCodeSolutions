class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = 0 
        for i in s:
            if i=="*":
                if l>0:
                    l-=1
            elif i=="#":
                l*=2
            elif i=="%":
                continue
            else:
                l+=1
        if k>=l:
            return "."
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c=="*":
                l+=1
            elif c=="#":
                l//=2
                if k>=l:
                    k-=l
            elif c=="%":
                k = l-1-k
            else:
                if k==l-1:
                    return c
                l-=1
        