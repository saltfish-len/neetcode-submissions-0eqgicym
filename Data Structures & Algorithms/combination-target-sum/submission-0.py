class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # each number has two cases: use or not
        # if use, reduce target and recurrent
        # if not, go to next number
        # iterate in increasing order can early stop when currnt num >target
        nums = sorted(nums)
        res = []
        def dfs(i, cur, combine):
            # i: current num's idx
            # cur: current sum before i
            # combine: current combination
            # edge case i>n
            if i >= len(nums):
                return
            num = nums[i]
            # early stop
            if num + cur > target:
                return
            
            if num + cur == target:
                res.append(combine+[num])
                # i+1 is too large
                return 
            if num + cur < target:
                # use i again
                dfs(i,cur+num,combine+[num])
                # skip i
                dfs(i+1,cur,combine)

            return
        dfs(0,0,[])
        return res
            