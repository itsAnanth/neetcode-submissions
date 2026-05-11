class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:

            hashid = [0] * 26

            for ch in s:
                hashid[ord(ch) - ord('a')] += 1

            hashid = tuple(hashid)
            if hashid not in m:
                m[hashid] = []

            m[hashid].append(s)
        
        return list(m.values())