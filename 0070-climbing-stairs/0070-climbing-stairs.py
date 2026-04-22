class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dp(n):
            if n in memo: return memo[n]

            if n == 0:
                return 1
            if n == 1:
                return 1
            memo[n] = dp(n-1) + dp(n-2) 
            return memo[n]
        
        def dp_2(n):
            memo = [0] * (n+1)
            memo[0], memo[1] = 1, 1

            for i in range(2, n+1):
                memo[i] = memo[i-1] + memo[i-2]

            return memo[n]

        return dp_2(n)
        