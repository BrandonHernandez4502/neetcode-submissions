class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        s = s.lower()
        i = len(s) - 1
        j = 0
        while i > j:
            if s[i] != s[j]:
                return False
            i -= 1
            j += 1
        return True