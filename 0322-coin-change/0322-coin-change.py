from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = defaultdict(float)

        def dp_down(n):

            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1

            res = float('INF')

            for c in coins:
                s = dp(n - c)
                if s == -1: continue
                res = min(res, s + 1)

            memo[n] = res if res != float('INF') else -1
            
            return memo[n]

        
        def dp_up(n):

            dp = [ amount + 1 ] * (amount + 1)
            dp[0] = 0

            for i in range(1, amount+1):
                for c in coins:
                    if i - c < 0: continue
                    dp[i] = min(dp[i], dp[i-c] + 1)
            
            return dp[amount] if dp[amount] != amount + 1 else -1


        
        return dp_up(amount)
        