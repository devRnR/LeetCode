class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, n):
            cur = max(prev1, prev2+nums[i])
            prev2, prev1 = prev1, cur
        
        return prev1

    

        