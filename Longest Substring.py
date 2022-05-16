from icecream import ic

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Length of string s
        len_s = len(s)
        if len_s == 1:
            return 1
        sub_str = ''
        for i in range(0, len_s-1):
            for j in range(i+1, len_s):
                # Find two repeating characters, filter by substring which only have one occur
                # e.g. bcabc should be filtered out
                if s[j] == s[i] and s[i:j].count(s[i]) == 1:
                    if self.unique_chars_set(s[0:i+1]) and len(s[0:i+1]) > len(sub_str):
                        sub_str = s[0:i+1]
                    if self.unique_chars_set(s[i:j]) and len(s[i:j]) > len(sub_str):
                        sub_str = s[i:j]
                    # 2nd pointer till the end
                    if self.unique_chars_set(s[j:len_s]) and len(s[j:len_s]) > len(sub_str):
                        sub_str = s[j:len_s]
        # Did not find any repeating character
        if sub_str == '':
            return len(s)
        else:
            return len(sub_str)

    # Returns if string has repeated word
    # https://stackoverflow.com/a/15751659
    def unique_chars_set(self, s):
        return len(s) == len(set(s))

# ic(Solution().lengthOfLongestSubstring('abcabcbb'))
# ic(Solution().lengthOfLongestSubstring('bbbbb'))
# ic(Solution().lengthOfLongestSubstring('pwwkew'))
# ic(Solution().lengthOfLongestSubstring(' '))
ic(Solution().lengthOfLongestSubstring('au'))
ic(Solution().lengthOfLongestSubstring('aab'))
# ic(Solution().lengthOfLongestSubstring('cdd'))
# ic(Solution().lengthOfLongestSubstring('abba'))