class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest_len = 0
        freq = {}
        most = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            most = max(most, freq[s[right]])

            while (right - left + 1) - most > k:
                freq[s[left]] -= 1
                left += 1

            longest_len = max(longest_len, right - left + 1)

        return longest_len