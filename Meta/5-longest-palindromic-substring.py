class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        count = 0
        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)
        return count