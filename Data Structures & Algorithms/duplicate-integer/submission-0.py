class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for v in count.values():
            if v > 1: return True
        return False