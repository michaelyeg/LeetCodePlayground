from icecream import ic

# Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        sub = {}
        for i in range(0, len(s)):
            for j in range(i+1, len(s)):
                # Find the position of the same letter in string
                if s[j] == s[i]:
                    sub_string = s[i:j]
                    if self.unique_chars_set(sub_string) is False:
                        continue
                    if s[i] not in sub or len(sub_string) > len(sub[s[i]]):
                        sub[s[i]] = sub_string
                    break
                else:
                    sub_string = s[i:j+1]
                    if self.unique_chars_set(sub_string) is False:
                        continue
                    if s[i] not in sub or len(sub_string) > len(sub[s[i]]):
                        sub[s[i]] = sub_string
        if len(sub) > 0:
            longest = max(sub.values(), key=len)
            return len(longest)
        else:
            return len(s)

    # Returns if string has repeated word
    # https://stackoverflow.com/a/15751659
    def unique_chars_set(self, s):
        return len(s) == len(set(s))


test = Solution()
ic(test.lengthOfLongestSubstring("au"))
ic(test.lengthOfLongestSubstring("abcabcbb"))
ic(test.lengthOfLongestSubstring("abcbbabc"))
ic(test.lengthOfLongestSubstring(" "))
ic(test.lengthOfLongestSubstring("bbbbb"))
ic(test.lengthOfLongestSubstring("pwwkew"))
ic(test.lengthOfLongestSubstring("aab"))
ic(test.lengthOfLongestSubstring("cdd"))
ic(test.lengthOfLongestSubstring("blqsearxxxbiwqa"))
