class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for word in strs:
            abc = [0]*26
            key = ""
            for char in word:
                abc[ord(char) - 'a'] += 1
            for num in abc:
                key += str(num)
            mpp[key] = word
        result = []
        for key, value in mpp:
            result.append(value)
        return result
        