class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, k in enumerate(nums):
            if k in d:
                return [d[k], i]
            d[target-k] = i

        