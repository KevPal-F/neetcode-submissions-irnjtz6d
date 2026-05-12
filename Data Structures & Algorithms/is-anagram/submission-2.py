class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for i in s:
            if i in ds:
                ds[i] += 1
            else:
                ds[i] = 1

        for i in t:
            if i in dt:
                dt[i] += 1
            else:
                dt[i] = 1

        for k in ds:
            if len(ds) != len(dt) or k not in dt or ds[k] != dt[k]: return False

        return True