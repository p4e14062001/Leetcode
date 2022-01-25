class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in cs:
                cs.remove(s[left])
                left = left + 1
            cs.add(s[right])
            res = max(res, right - left + 1)
        return res
