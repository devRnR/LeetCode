class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dp(n):
            memo = [0] * (amount + 1)
            memo[0] = 1
            
            for c in coins:
                for x in range(c, amount +1):
                    memo[x] += memo[x-c]
            
            return memo[n]

        return dp(amount)