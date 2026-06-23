class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            t2 = target - nums[i]
            if t2 in mp:
                return [i,mp[t2]]
            mp[nums[i]] = i
        
        
