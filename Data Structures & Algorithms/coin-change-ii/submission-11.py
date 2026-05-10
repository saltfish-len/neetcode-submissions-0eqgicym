class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        def dfs(a,i):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if (a,i) in cache:
                return cache[(a,i)]
            res = 0
            if a >= coins[i]:
                # if coins[i] < a, we cannot use it then return res=0
                res += dfs(a-coins[i], i) # use
                res += dfs(a,i+1) # don't use
            # cache
            cache[(a,i)] = res
            return res
        
        return dfs(amount,0)