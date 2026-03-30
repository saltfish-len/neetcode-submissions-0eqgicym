class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        # check if start
        lc = 0
        for x in nums:
            if x-1 not in numset:
                # x is a start
                l = 0
                y = x
                while y in numset:
                    l+=1
                    y+=1
                lc = max(lc,l) 

        return lc