class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for char in s:
            if char not in t or len(s) != len(t):
                return False
        return True
        