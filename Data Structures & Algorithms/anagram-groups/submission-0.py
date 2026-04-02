class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDic = {}
        anagramList = []

        for i in strs:
            arrangedStr = "".join(sorted(i))

            if arrangedStr not in anagramDic:
                anagramDic[arrangedStr] = [i]
            
            else:
                anagramDic[arrangedStr] += [i]
        
        for k in anagramDic:
            anagramList += [anagramDic[k]]

        return anagramList
        