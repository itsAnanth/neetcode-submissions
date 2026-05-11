class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {}

        for i, num in enumerate(nums):
            
            tofind = target - num

            if tofind in m:
                return [m[tofind], i]

            m[num] = i