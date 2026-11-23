class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cache = {} # comniantion until i th
        n = len(s)
        def check(i,j):
            # s[i:j]
            while i < j:
                if s[i] != s[j-1]:
                    return False
                i+=1
                j-=1
            return True
        res = []
        def dfs(i,j,cur):
            if j > n:
                if i == j-1:
                    res.append(cur.copy())
                return
            if check(i,j):
                # cut
                cur.append(s[i:j])
                dfs(j,j+1,cur)
                cur.pop(-1)
            # skip
            dfs(i,j+1,cur)
        
        dfs(0,1,[])
        return res
            