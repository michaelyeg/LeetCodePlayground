from icecream import ic

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ''
        length = self.getGcdLength(len(str1), len(str2))

        if len(str1) >= len(str2):
            gcd = str2[0:length]

        else:
            gcd = str1[0:length]

        if str1 == gcd * (len(str1) // length) and str2 == gcd * (len(str2) // length):
            return gcd

        return ''
    # Calculate the largest common divisor of two numbers
    def getGcdLength(self, str1len: int, str2len: int):
        gcd = 0
        for i in range(1, min(str1len, str2len)+1):
            if str1len % i == 0 and str2len % i == 0:
                gcd = i
        return gcd

ic(Solution().gcdOfStrings("ABCABC", "ABC"))
ic(Solution().gcdOfStrings("ABABAB", "ABAB"))
ic(Solution().gcdOfStrings("LEET", "CODE"))
ic(Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
ic(Solution().gcdOfStrings("AA", "A"))
