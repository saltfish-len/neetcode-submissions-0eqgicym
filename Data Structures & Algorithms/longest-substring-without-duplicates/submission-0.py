class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if n == 0:
            return 0
        l = 0
        r = 0
        length = 0
        index = {}
        while r < n:
            # extend r
            if index.get(s[r],-1) == -1:
                index[s[r]] = r
                r+=1
                length = max(r-l,length)
            else:
                # move l to first s[r]
                new_l = index[s[r]] + 1
                for i in range(l,new_l):
                    index[s[i]] = -1
                l = new_l
                
        return length
