from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = defaultdict(float)

        def dp(n):

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
        
        return dp(amount)
        