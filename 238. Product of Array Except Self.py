from functools import reduce
from typing import List
from icecream import ic

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for ct, vl in enumerate(nums):
            pro = reduce(lambda x, y: x*y, nums[:ct] + nums[ct+1:]) if 0 not in nums[:ct] + nums[ct+1:] else 0
            res.append(pro)
        return res

ic(Solution().productExceptSelf([1,2,3,4]))
ic(Solution().productExceptSelf([-1,1,0,-3,3]))
