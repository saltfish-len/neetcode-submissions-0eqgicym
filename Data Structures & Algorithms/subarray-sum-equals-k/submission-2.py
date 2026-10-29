class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        n = len(nums)
        prefix = [0] * (n+1)
        summation = 0
        for i in range(n):
            summation += nums[i]
            prefix[i+1] += summation
        
        # we can use prefix to search sum[i,j] in O(1)
        ct = defaultdict(int)
        ct[0] = 1
        res = 0
        for i in range(1,n+1):
            diff = prefix[i] - k
            res += ct[diff]
            ct[prefix[i]] += 1
        return res
            