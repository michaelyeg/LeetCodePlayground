# https://leetcode.com/problems/reverse-integer/
from icecream import ic

class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        if x == 0:
            return x
        elif x < 0:
            res += '-'
            x = abs(x)
        # Convert int x to list with each digit
        x_l = []
        while x != 0:
            z = x % 10
            x_l.append(z)
            x = x // 10
        # 123 -> [3, 2, 1]
        for i in range(len(x_l)):
            res += str(x_l[i])
        res_int = int(res)
        if res_int > 2**31-1 or res_int < -2**31:
            return 0
        return res_int


test = Solution()
ic(test.reverse(123))
ic(test.reverse(-123))
ic(test.reverse(120))
ic(test.reverse(0))
ic(test.reverse(1534236469))