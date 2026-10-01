class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        # can conver to set as each element exists only once in LC
        nums = set(nums)
        for s in nums:
            if s-1 in nums:
                continue
            l = 1
            x = s
            while x+1 in nums:
                l += 1
                x += 1
            res = max(res,l)

        return res
        
