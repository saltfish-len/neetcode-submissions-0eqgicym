class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = set()
        def dfs(i, cur_sum, cur_comb):
            if i>=len(candidates):
                return
            num = candidates[i]
            if num+cur_sum > target:
                # early stop
                return
            
            if num+cur_sum == target:
                res.add(tuple(cur_comb+[num]))
                # skip i
                dfs(i+1,cur_sum,cur_comb)
            
            if num+cur_sum < target:
                # use i
                dfs(i+1,cur_sum+num,cur_comb+[num])
                # not use i
                dfs(i+1,cur_sum,cur_comb)

        dfs(0,0,[])
        return [list(r) for r in res]