class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash by # of char
        res = dict()
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')] += 1
            k = tuple(key)
            res[k] = res.get(k, [])
            res[k].append(s)

        return list(res.values())