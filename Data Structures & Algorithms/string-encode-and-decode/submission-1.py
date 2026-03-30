class Solution:

    def encode(self, strs: List[str]) -> str:
        # length + # + string
        if len(strs) == 0: return "#"
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        if s == "#": return []
        def cut(string):
            sharp_index = string.index("#")
            length = int(string[:sharp_index])
            if length == 0:
                first = ''
            else:
                first = string[sharp_index+1:][:length]
            if len(string) <= sharp_index+1+length:
                return first, None
            left = string[sharp_index+1+length:]
            return first, left
        res = []
        l = s
        while l is not None:
            f,l = cut(l)
            res.append(f)
        return res