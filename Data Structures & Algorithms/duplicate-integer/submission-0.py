class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        
        #or
        """
        seen = set()   empty set
        
        for n in nums:
            if num in seen:    check if n in set
                return True
            seen.add(n).   add n to set
        return Flase
        """
