class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo:dict[int, int] = {}
        INF = float('INF')

        def dp_down(n):

            if n == 0: return 0
            if n in memo: return memo[n]

            res = +INF

            for c in coins:
                if n - c < 0: continue
                res = min(res, dp_down(n - c) + 1)
            
            memo[n] = res
            return res

        
        def dp_up(n):

            dp = [ amount + 1 ] * (amount + 1)
            dp[0] = 0

            for i in range(1, amount+1):
                for c in coins:
                    if i - c < 0: continue
                    dp[i] = min(dp[i], dp[i-c] + 1)
            
            return dp[amount] if dp[amount] != amount + 1 else -1

        ans = dp_down(amount)
        return -1 if ans == INF else ans
        