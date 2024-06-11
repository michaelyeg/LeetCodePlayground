from icecream import ic
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        result_len = len(word1) + len(word2)
        for i in range(result_len):
            if i % 2 == 0:
                if len(word1) > 0:
                    result += word1[0]
                    word1 = word1[1:]
                elif len(word2) > 0:
                    result += word2[0]
                    word2 = word2[1:]
            else:
                if len(word2) > 0:
                    result += word2[0]
                    word2 = word2[1:]
                elif len(word1) > 0:
                    result += word1[0]
                    word1 = word1[1:]
        return result

ic(Solution().mergeAlternately("abc","pqr"))
ic(Solution().mergeAlternately("ab","pqrs"))
ic(Solution().mergeAlternately("abcd","pq"))