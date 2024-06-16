from icecream import ic

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        # Find all vowels index
        vowel_index = [i for i, char in enumerate(s) if char in vowels]
        vowel_index_c = vowel_index.copy()
        s_cpy = s
        for i in vowel_index:
            s = s[0:i] + s_cpy[vowel_index_c.pop()] + s[i+1:]
        return s

ic(Solution().reverseVowels("hello"))
ic(Solution().reverseVowels("leetcode"))