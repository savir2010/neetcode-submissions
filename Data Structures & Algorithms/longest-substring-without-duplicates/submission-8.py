class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        window_size = 0
        for p2 in range(len(s)):
            while s[p2] in s[p1:p2]:
                p1 += 1
            
            window_size = max(window_size,(p2+1)-p1)
        
        return window_size