from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            abc = [0]*26
            for char in word:
                abc[ord(char) - ord('a')] += 1
            
            key = tuple(abc)
            groups[key].word

        return list(mpp.values())