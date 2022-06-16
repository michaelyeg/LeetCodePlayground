# https://leetcode.com/problems/longest-string-chain/
from typing import List
from icecream import ic


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chain = []
        # sort words by length
        words = sorted(words, key=len)

        for i in range(0, len(words) - 1):
            chain_new = [words[i]]
            for j in range(i + 1, len(words)):
                if self.isChain(chain_new[-1], words[j]):
                    chain_new.append(words[j])
                # Allow tail overwritten
                elif len(chain_new) >= 2 and self.isChain(chain_new[-2], words[j]):
                    chain_new[-1] = words[j]
            # Search for previous words to see if longer chain is possible
            for k in range(i, -1, -1):
                if self.isChain(words[k], chain_new[0]):
                    chain_new.insert(0, words[k])
            # ic(chain_new)
            if len(chain_new) > len(chain):
                chain = chain_new
        return len(chain)

    def isChain(self, word1: str, word2) -> bool:
        if len(word2) != len(word1) + 1:
            return False
        len_word1 = len(word1)
        len_word2 = len(word2)
        if word1[0:len_word1] == word2[0:len_word1] or word1[0:len_word1] == word2[1:len_word2]:
            return True
        for i in range(len_word1):
            if word1[0:i] == word2[0:i] and word1[i:len_word1] == word2[i + 1:len_word2]:
                return True
        return False


test = Solution()
ic(test.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
ic(test.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
ic(test.longestStrChain(["abcd", "dbqca"]))
ic(test.longestStrChain(["a", "ab", "ac", "bd", "abc", "abd", "abdd"]))
ic(test.longestStrChain(
    ["b", "vb", "ktttrh", "rvqby", "kttrh", "bktttirhx", "bktttrh", "rvqb", "ktrh", "rvb", "bktttrhx", "cbktttirhx"]))
