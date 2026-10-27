class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # convert to interval overlap
        mp = {} # char: [start_ids, end_idx]
        prev = 0 # last substring end
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = [i,i]
            else:
                mp[s[i]][1] = max(i, mp[s[i]][1])
        
        n = len(s)
        res = []
        i = 0
        start = 0
        end = mp[s[0]][1]
        while i < n:
            start = i
            end = max(mp[s[i]][1],end)
            while i < end:
                end = max(mp[s[i]][1],end)
                i+=1 
            # i = end
            res.append(i-start+1)
            i += 1
        return res


        
