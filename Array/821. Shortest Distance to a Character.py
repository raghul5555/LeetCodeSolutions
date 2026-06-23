class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        c_index = []
        for i in range(len(s)):
            if s[i]==c:
                c_index.append(i)
        sol = []
        j = 0
        for i in range(len(s)):
            if s[i]==c:
                sol.append(0)
                j+=1
            elif i<c_index[0]:
                sol.append(c_index[0]-i)
            elif i>c_index[-1]:
                sol.append(i-c_index[-1])
            else:
                sol.append(min(c_index[j]-i, i-c_index[j-1]))
        return sol