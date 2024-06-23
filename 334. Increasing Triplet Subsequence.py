from typing import List
from icecream import ic

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False

        first, second = float('inf'), float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

ic(Solution().increasingTriplet([1,2,3,4,5]))
ic(Solution().increasingTriplet([5,4,3,2,1]))
ic(Solution().increasingTriplet([2,1,5,0,4,6]))
ic(Solution().increasingTriplet([1,2,2,1]))
ic(Solution().increasingTriplet([1,5,0,4,1,3]))
ic(Solution().increasingTriplet([1,6,2,5,1]))