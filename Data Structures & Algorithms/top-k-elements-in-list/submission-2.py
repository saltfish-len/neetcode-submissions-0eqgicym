class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 0
            else:
                count[x] += 1

        
        n = len(nums)
        freq_bucket = [[] for _ in range(n)]
        for key,val in count.items():
            freq_bucket[val].append(key)
        res = []
        for i in reversed(range(n)):
            for x in freq_bucket[i]:
                res.append(x)
                if len(res)==k:
                    return res