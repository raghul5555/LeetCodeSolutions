class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        mp1 = {}
        for i in p:
            mp1[i] = mp1.get(i, 0) + 1
        mp2 = {}
        sol = []
        k = len(p)
        for i in range(len(s)-k+1):
            if i==0:
                for j in range(k):
                    mp2[s[j]] = mp2.get(s[j], 0) + 1
                if mp1==mp2:
                    sol.append(i)
            else:
                mp2[s[i-1]] -= 1
                mp2[s[i+k-1]] = mp2.get(s[i+k-1], 0) + 1
                if mp2[s[i-1]]==0:
                    mp2.pop(s[i-1])
                if mp2==mp1:
                    sol.append(i)
        return sol              