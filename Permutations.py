# https://leetcode.com/problems/permutations/
from typing import List
from icecream import ic


class Solution:
    # https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        res = []
        for perm in self.permute(nums[1:]):
            for i in range(len(nums)):
                res.append(perm[:i] + nums[0:1] + perm[i:])
        return res


test = Solution()
ic(test.permute([0, 1]))
ic(test.permute([1]))
ic(test.permute([]))
ic(test.permute([1, 2, 3]))
