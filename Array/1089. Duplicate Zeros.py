class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while(i<len(arr)):
            if arr[i]==0 and i!=(len(arr)-1):
                t = arr[i+1]
                arr[i+1] = 0
                for j in range(i+2,len(arr)):
                    temp = arr[j]
                    arr[j] = t
                    t = temp
                i+=1
            i+=1
        
        