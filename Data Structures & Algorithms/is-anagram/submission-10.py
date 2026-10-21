class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        abc = [0] * 26
        for x, y in zip(s, t):
            abc[ord(x) - ord('a')] += 1
            abc[ord(y) - ord('a')] -= 1
        for num in abc:
            if num != 0:
                return False
        return True
