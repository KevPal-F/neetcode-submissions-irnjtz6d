class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = []
        d = {}
        for key in nums:
            if key in d:
                d[key] += 1
            else:
                d[key] = 1

        # List of [(num, freq), ...]
        # ex. d.items(): [(2, 2), (3, 3), (1, 1)] -> [(3, 3), (2, 2), (1, 1)]
        sortedDict = sorted(d.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            freqList.append(sortedDict[i][0])

        return freqList