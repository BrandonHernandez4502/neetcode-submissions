class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for c in s:
            if c.isalnum():
                new += c.lower()

        i = len(new) - 1
        j = 0
        while i > j:
            if new[i] != new[j]:
                return False
            i -= 1
            j += 1
        return True