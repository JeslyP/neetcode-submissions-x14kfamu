class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in value_map:
                return [value_map[diff], i]

        
            value_map[n] = i
