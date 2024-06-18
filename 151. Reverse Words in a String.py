from icecream import ic

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = [word for word in words if word]
        reversed_string = " ".join(reversed(words))
        return reversed_string

ic(Solution().reverseWords("the sky is blue"))
ic(Solution().reverseWords("  hello world  "))
ic(Solution().reverseWords("a good   example"))