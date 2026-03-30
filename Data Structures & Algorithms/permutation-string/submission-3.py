class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide a window with size len(s1) and count chars.
        if len(s1) > len(s2):
            return False
        
        tgt = Counter(s1) 
        w = len(s1)
        count = Counter(s2[:w])
        if count == tgt: return True
        for l in range(1,len(s2)-w+1):
            # remove l-1, add r
            count[s2[l-1]] -= 1
            if count[s2[l-1]] == 0:
                count.pop(s2[l-1])
            # add r
            r = l+w-1
            count[s2[r]] = count.get(s2[r],0)+1
            # check
            if count == tgt: return True
        return False