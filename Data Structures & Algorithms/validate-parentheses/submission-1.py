class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch not in bracketmap:
                stack.append(ch)
            else:
                if stack and stack[-1] == bracketmap[ch]:
                    stack.pop()
                else:
                    return False
        return not stack