class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        for i  in range(0,len(s)):
            seen = set()
            for j in range(i , len(s)):
                if s[j] in seen:
                    break
      
                seen.add(s[j])
                current_len = j-i+1
                max_count = max(max_count , current_len)

        return max_count
