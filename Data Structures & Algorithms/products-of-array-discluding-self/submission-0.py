class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        n = len(nums)

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1

        if zero_cnt > 1:
            return [0] * n

        res = [0] * n
        for i, num in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num

        return res
            