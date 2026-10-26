class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # counting
        from collections import defaultdict
        count = defaultdict(int)
        for x in nums:
            count[x] += 1
        res = set()
        for x in nums:
            count[x] -= 1
            for y in nums:
                if count[y]: # zero means y is x
                    # solve two sum
                    count[y] -= 1
                    z = -(x+y)
                    if count[z]:
                        res.add(tuple(sorted([x,y,z])))
                    count[y] += 1
            count[x] += 1

        return list(res)