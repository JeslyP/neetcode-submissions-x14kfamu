class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                print (f'True {nums[i]}')
                return True

            else:
                seen.add(nums[i])
                print (f' Else {nums[i]}')
        return False
                 