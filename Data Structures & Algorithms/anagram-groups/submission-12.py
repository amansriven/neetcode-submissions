class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        
        for word in strs:
            abc = [0] * 26
            for c in word:
                abc[ord(c) - ord('a')] += 1
            count = tuple(abc)
            if count in freq:
                freq[count].append(word)
            else:
                freq[count] = [word]

        return list(freq.values())