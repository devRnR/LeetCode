class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        memo = [-1 for _ in range(n)]

        for i in range(n):

            target = nums[i]
            limit = (i + 1) % n

            while limit != i:
                if nums[limit] > target:
                    memo[i] = nums[limit]
                    break
                
                limit = (limit + 1) % n
        
        return memo

