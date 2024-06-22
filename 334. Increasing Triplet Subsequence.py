from typing import List
from icecream import ic

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3 or all(x == nums[0] for x in nums): return False
        for i in range(0, len(nums)-2):
            j = i+1
            k = j+1
            while j < len(nums)-1 and k < len(nums):
                if nums[i] < nums[j] < nums[k]: return True
                if j == len(nums)-2 and k == len(nums)-1:
                    break
                if nums[i] >= nums[j]:
                    j+=1
                    k=j+1
                    continue
                if k < len(nums)-1:
                    k+=1
                    continue
                if j < len(nums)-2:
                    j+=1
                    if k == len(nums)-1:  k=j+1
                    continue
        return False

ic(Solution().increasingTriplet([1,2,3,4,5]))
ic(Solution().increasingTriplet([5,4,3,2,1]))
ic(Solution().increasingTriplet([2,1,5,0,4,6]))
ic(Solution().increasingTriplet([1,2,2,1]))
ic(Solution().increasingTriplet([1,5,0,4,1,3]))
ic(Solution().increasingTriplet([1,6,2,5,1]))