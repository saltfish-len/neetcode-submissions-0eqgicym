class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if one half is sorted, the minimun is in the other side
        # check unsorted by nums[l] > nums[r]
        l = 0
        r = len(nums)-1
        res = min(nums[l], nums[r])
        while l<=r:
            # if current window is sorted, l is min
            if nums[l] < nums[r]:
                return min(nums[l],res)
            m = (l+r)//2
            res = min(nums[m],res)
            if nums[l] > nums[m]:
                # unsorted, min in [l...m]
                r = m-1
            else:
                # m...r unsorted
                l = m+1
        return res





