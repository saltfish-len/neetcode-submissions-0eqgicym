class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_hash(s):
            # convert s to a touple len 26
            h = [0] * 26
            for x in s:
                h[ord(x)-ord('a')]+=1
            return tuple(h)

        res = defaultdict(list)
        for s in strs:
            res[create_hash(s)].append(s)
        return list(res.values())


