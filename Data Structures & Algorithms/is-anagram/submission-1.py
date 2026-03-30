class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count_s = Counter(s)
        count_t = Counter(t)
        for k in count_s.keys():
            if count_s[k] != count_t.get(k,None):
                return False
        return True