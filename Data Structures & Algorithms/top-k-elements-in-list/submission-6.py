class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        # sort key by value
        keys = list(count.keys())
        keys = sorted(keys, key = lambda x:count[x], reverse=True)
        return keys[:k]