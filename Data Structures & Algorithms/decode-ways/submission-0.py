class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}

        def dfs(i):
            if i >= len(s):
                mem[i] = 1
                return 1
            if s[i] == '0':
                mem[i] = 0
                return 0
            if i in mem.keys():
                return mem[i]
            if i < len(s) - 1:
                if (s[i] == '1' or 
                    (s[i] == '2' and 
                    s[i + 1] < '7')):
                    res =  dfs(i+1) + dfs(i+2)
                    mem[i] = res
                    return res
            res = dfs(i+1)
            mem[i] = res
            return res

        return dfs(0)