class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        memo = [-1 for _ in range(n)]

        for i in range(2*n-1, -1, -1):
            idx = i % n

            while stack and stack[-1] <= nums[idx]:
                stack.pop()
            
            if i < n and stack:
                memo[i] = stack[-1]

            stack.append(nums[idx])
            

        return memo

