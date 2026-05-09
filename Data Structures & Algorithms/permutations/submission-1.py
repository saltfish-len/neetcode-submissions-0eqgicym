class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perm = self.permute(nums[1:])
        x = nums[0]
        res = []
        for p in perm:
            for i in range(len(nums)):
                new = p.copy()
                new.insert(i,x)
                res.append(new)
        return res


        