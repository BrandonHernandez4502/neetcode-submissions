class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT,  stackIdx = stack.pop()
                res[stackIdx] = (idx - stackIdx)
            stack.append([temp, idx])
        return res