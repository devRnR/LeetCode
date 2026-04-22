class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dp(n):
            memo = [0] * (amount + 1)
            memo[0] = 1
            
            for c in coins:
                for x in range(c, amount +1):
                    memo[x] += memo[x-c]
            
            return memo[n]
        
        memo = {}
        def dp_recur(n, i):
            if n== 0:
                return 1
            if n < 0 or i == len(coins):
                return 0
            

            key = (i, n)
            if key in memo:
                return memo[key]
            
            res = dp_recur(n, i+1)
            res += dp_recur(n - coins[i], i)

            memo[key] = res

            return res

        return dp_recur(amount, 0)