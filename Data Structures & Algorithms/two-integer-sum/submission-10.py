class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicmap = {}
        
        for i, n in enumerate(nums):
            remained = target - n

            if remained in dicmap:
                return [dicmap[remained], i]

            dicmap[n] = i
