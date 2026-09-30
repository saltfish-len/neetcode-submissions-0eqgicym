class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1

        freq_sort = sorted(list(count.keys()), key=lambda x: count[x], reverse=True)
        return freq_sort[:k]

