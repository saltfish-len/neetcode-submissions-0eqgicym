class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # use or not use
        res = set()

        def dfs(idx, subset):
            # idx: current index to decide
            if idx == len(nums):
                # all num itered
                res.add(tuple(subset))
                return 

            
            # use nums[i]
            subset.append(nums[idx])
            dfs(idx+1, subset)
            # skip nums[i]
            subset.pop()
            dfs(idx+1,subset)
        
        nums.sort()
        dfs(0,[])
        return [list(s) for s in res]
            
