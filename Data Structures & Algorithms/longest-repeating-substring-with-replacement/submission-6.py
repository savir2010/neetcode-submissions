class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest_len = 0
        freq = {}
        most = 0

        for right in range(len(s)):
            # Add the current character to the window
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Track the highest frequency in the current window
            most = max(most, freq[s[right]])

            # Number of replacements needed is:
            # window length - count of the most frequent character
            while (right - left + 1) - most > k:
                freq[s[left]] -= 1
                left += 1

            # Current window is valid
            longest_len = max(longest_len, right - left + 1)

        return longest_len