class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        for j in range(0, k):
            currBestVal = 0
            currBestKey = None
            for key, value in counts.items():
                if value > currBestVal:
                    currBestVal = value
                    currBestKey = key
            output.append(currBestKey)
            counts.pop(currBestKey, None)

        return output
            