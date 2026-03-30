class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide a window with size len(s1) and count chars.
        # edge case
        if len(s1) > len(s2):
            return False
        idxmap = lambda ch:ord(ch) - ord('a')

        # hash table
        h1 = [0] * 26
        h2 = [0] * 26
        for ch in s1:
            idx = idxmap(ch)
            h1[idx] += 1

        match = 0 # number of matched char, if 26, return true

        # sliding window init
        w = len(s1) # width
        l = 0 # left pointer
        r = l+w
        for ch in s2[l:r]:
            idx = idxmap(ch)
            h2[idx] += 1
        # check for the first window, init match
        for c1, c2 in zip(h1,h2):
            match += 1 if c1 == c2 else 0
        if match == 26:
            return True

        for l in range(1,len(s2)-w+1): # last window s2[r] r=len l=len-w
            r = l+w-1
            # remove left
            idx = idxmap(s2[l-1])
            h2[idx] -= 1
            # check
            if h1[idx] == h2[idx]:
                match += 1
            elif h1[idx] == h2[idx]+1:
                # make worse
                match -= 1
            
            # add right
            idx = idxmap(s2[r])
            h2[idx] += 1
            # check
            if h1[idx] == h2[idx]:
                match += 1
            elif h1[idx]== h2[idx]-1:
                # make worse
                match -= 1
            
            if match == 26:
                return True
        return False