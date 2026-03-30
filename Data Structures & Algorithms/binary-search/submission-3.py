class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l<=r:
            m = l+ ((r-l)//2)
            mid_num = nums[m]
            if target == mid_num:
                return m
            if target < mid_num:
                r = m-1
            if target > mid_num:
                l = m+1
        
        return -1
