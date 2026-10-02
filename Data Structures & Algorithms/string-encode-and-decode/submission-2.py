class Solution:

    def encode(self, strs: List[str]) -> str:
        # length: str
        return ''.join([str(len(s))+':'+s for s in strs])
    
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        prev = 0
        res = []
        while i<n:
            # first ':'
            while s[i] != ':':
                i += 1
                continue
            # s[i] == ':'
            length = int(s[prev:i]) # ':' + len(str)
            end = i+length
            x = s[i+1:end+1]
            res.append(x)
            i = end+1
            prev = i
        return res
