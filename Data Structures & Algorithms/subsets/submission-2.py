class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # include it or exclude it.
        res = []
        subset = []

        def dfs(i):
            # i is the number of assigned elm
            if i >= len(nums):
                # no more subset
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            # keep i
            dfs(i+1)
            subset.pop()
            # i finished
            dfs(i+1)
            return
        
        dfs(0)
        return res