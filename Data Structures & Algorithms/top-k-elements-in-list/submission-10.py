class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max freq = len(nums)
        # sort by freq

        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        # bucket sort
        freq = [[] for _ in nums]
        for key,val in count.items():
            freq[val-1].append(key)
        
        # build res
        res = []
        for key in reversed(freq):
            res+=key
            if len(res) >= k:
                break
        return res[:k]