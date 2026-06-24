class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_map = {}
        for i in s1:
            s1_map[i] = s1_map.get(i, 0) + 1
        win_map = {}
        for i in range(len(s2)-len(s1)+1):
            if i==0:
                for j in range(len(s1)):
                    win_map[s2[j]] = win_map.get(s2[j], 0) + 1
                if win_map==s1_map:
                    return True
            else:
                win_map[s2[i-1]] -= 1
                if win_map[s2[i-1]]==0:
                    win_map.pop(s2[i-1])
                win_map[s2[i+len(s1)-1]] = win_map.get(s2[i+len(s1)-1], 0) + 1
                if win_map == s1_map:
                    return True
            print(s1_map, win_map, i)
        return False