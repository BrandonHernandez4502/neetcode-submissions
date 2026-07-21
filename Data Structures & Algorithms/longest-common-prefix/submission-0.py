class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for chars in zip(*strs):
            if len(set(chars)) != 1:
                return ''.join(res)
            res.append(chars[0])
        return ''.join(res)