class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times = defaultdict(int)
        for num in nums:
            times[num] += 1
        # num: times
        # binsort
        freq_idx = [list() for _ in nums]
        for i,v in times.items():
            freq_idx[v-1].append(i)
        
        res = []
        for num_list in reversed(freq_idx):
            res+= num_list
            if len(res) >= k:
                return res
            
