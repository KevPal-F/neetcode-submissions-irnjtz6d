class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charDic = {}
        anagramList = []

        for i in strs:
            charCount = [0] * 26
            for c in i:
                charCount[ord(c) - 97] += 1

            key = tuple(charCount)
            if key not in charDic:
                charDic[key] = [i]
            
            else:
                charDic[key] += [i]

        for k in charDic:
            anagramList += [charDic[k]]

        return anagramList