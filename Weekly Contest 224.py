from icecream import ic
import random
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        products = {}
        for i in range(0, len(nums)-1):
            for j in range(1, len(nums)):
                if i < j:
                    p = nums[i] * nums[j]
                    if p not in products:
                        products[p] = 1
                    else:
                        products[p] += 1
        valid = 0
        for (key, value) in products.items():
            if value > 1:
                sum = value * (value - 1) // 2
                valid += sum
        return valid * 8

test = Solution()
ic(test.tupleSameProduct([2,3,4,6,8,12]))
