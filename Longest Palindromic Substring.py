# https://leetcode.com/problems/longest-palindromic-substring/
from icecream import ic


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # odd length
            res = self.getPalindrome(i, i, res, s)
            # even length
            res = self.getPalindrome(i, i + 1, res, s)
        return res

    # Scan the string given starting index, if match then expand
    def getPalindrome(self, j, k, res, s):
        while j >= 0 and k < len(s):
            if k - j + 1 > len(res) and s[j] == s[k]:
                res = s[j:k + 1]
            # If two chars does not match, break & exit
            if j != k and s[j] != s[k]:
                break
            j -= 1
            k += 1
        return res


test = Solution()
ic(test.longestPalindrome('babad'))
ic(test.longestPalindrome('cbbd'))
ic(test.longestPalindrome('aacabdkacaa'))
