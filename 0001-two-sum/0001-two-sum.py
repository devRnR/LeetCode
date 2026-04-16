class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            v = target - num
            if v in memo:
                return [memo[v], i]
            memo[num] = i