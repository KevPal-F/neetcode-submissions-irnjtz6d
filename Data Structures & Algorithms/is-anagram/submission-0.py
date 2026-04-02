class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s) != len(t): return False

        for k in s:
            if k not in d:
                d[k] = 0
            d[k] += 1
        
        for k in t:
            if k not in d: return False
            d[k] -= 1
            if d[k] < 0: return False

        for k in d:
            if d[k] != 0: return False    
        
        return True