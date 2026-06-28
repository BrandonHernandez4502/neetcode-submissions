class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        best = 0
        while i < j:
            h = min(heights[i], heights[j])
            res = h * (j - i)
            best = max(best, res)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return best