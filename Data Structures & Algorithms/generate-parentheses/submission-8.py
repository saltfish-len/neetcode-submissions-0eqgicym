class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def dfs(idx, par):
            if idx == n:
                res.add(par)
                return
            for i in range(len(par)+1):
                dfs(idx+1,par[:i]+'()'+par[i:])
        
        dfs(1,"()")
        return list(res)