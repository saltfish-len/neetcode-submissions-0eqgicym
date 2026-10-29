class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointer
        # expand window when not enough
        # shorten it when have extra

        cntt = defaultdict(int)
        for x in t:
            cntt[x] += 1

        window = defaultdict(int)
        included = 0
        tt = len(t)
        res = [-1, len(s)]
        l = 0 # window [l, r]
        for r in range(len(s)):
            # add s[r] to window
            window[s[r]] += 1
            if window[s[r]] <= cntt[s[r]]:
                included += 1 
            # check if l is removeable
            while l <= r and window[s[l]] > cntt[s[l]]:
                window[s[l]] -= 1
                l += 1
            if included == tt:
                if r-l < res[1]-res[0]:
                    res = [l,r]
            
        return s[res[0]:res[1]+1] if res[0] >= 0 else ''


