from typing import List
from icecream import ic

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]


ic(Solution().kidsWithCandies([2,3,5,1,3], 3))
ic(Solution().kidsWithCandies([4,2,1,1,2], 1))
ic(Solution().kidsWithCandies([12,1,12], 10))