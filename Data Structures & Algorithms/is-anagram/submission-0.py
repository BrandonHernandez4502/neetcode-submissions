class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        if len(s) != len(t):
            return False
        for i in range(0, len(t)):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True