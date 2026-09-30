class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        
        n = len(nums)
        freq_bucket = [[] for _ in range(n)]
        for key,val in count.items():
            freq_bucket[val-1].append(key)
        res = []
        for i in reversed(range(n)):
            for x in freq_bucket[i]:
                res.append(x)
                if len(res)==k:
                    return res