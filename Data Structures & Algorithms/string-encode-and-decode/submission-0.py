class Solution:

    def encode(self, strs) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str):
        strs = []
        i = 0

        while i < len(s):
            length = 0
            while s[i] != '#':
                length = length * 10 + int(s[i])
                i += 1

            i += 1

            strs.append(s[i:i+length])

            i += length

        return strs