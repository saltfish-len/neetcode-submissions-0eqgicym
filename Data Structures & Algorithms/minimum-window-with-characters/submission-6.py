class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "":
            return ""
        res = ""
        reslen = len(s)+1

        countT, window = {}, {}
        for x in t:
            countT[x] = countT.get(x,0) + 1
        
        have = 0
        need = len(t)


        l = 0
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] = window.get(s[r],0) + 1
                if window[s[r]] <= countT[s[r]]:
                    # not extra
                    have += 1
            while have == need and l <= r:
                # vaild window
                # move l
                if r-l+1 < reslen:
                    res = s[l:r+1]
                    reslen = len(res)
                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        # not extra
                        have -= 1
                        
                l += 1
        return res

            


        