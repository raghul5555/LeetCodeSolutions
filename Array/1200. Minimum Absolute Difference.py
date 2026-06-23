class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dif = arr[1] - arr[0]
        
        for i in range(1, len(arr)-1):
            if (arr[i+1] - arr[i]) < min_dif:
                min_dif = arr[i+1] - arr[i]
        
        sol = []
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) == min_dif:
                sol.append([arr[i], arr[i+1]])
                
        return sol
        