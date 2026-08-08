class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen =set()
        l=0
        long_substring =0

        for r in range(0 , len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l=l+1

            seen.add(s[r])

            long_substring = max(long_substring , r-l+1)

        return long_substring
        