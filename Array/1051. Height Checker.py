class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = [i for i in heights]
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(expected)-1):
                if expected[i] > expected[i+1]:
                    expected[i], expected[i+1] = expected[i+1], expected[i]
                    swapped = True
        c = 0
        for i in range(len(expected)):
            if heights[i] != expected[i]:
                c+=1
        return c
            