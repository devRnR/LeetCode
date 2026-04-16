class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        cur_l = 1
        for i in range(n):
            answer[i] = cur_l
            cur_l *= nums[i]
        
        cur_r = 1
        for i in range(n-1, -1, -1):
            answer[i] *= cur_r
            cur_r *= nums[i]
        
        return answer
        