class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        
        k = [0] * 26

        for si, st in zip(s, t):

            k[ord(si) - ord('a')] += 1
            k[ord(st) - ord('a')] -= 1


        return all(n == 0 for n in k)