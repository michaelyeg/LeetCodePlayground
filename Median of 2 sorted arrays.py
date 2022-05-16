from typing import List
from icecream import ic

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Cache the index of nums1
        if len(nums1) == 0:
            nums1 = nums2
        else:
            min = 0
            # Insert nums2 into nums1
            for i in range(0, len(nums2)):
                for j in range(min, len(nums1)):
                    if nums2[i] <= nums1[j]:
                        nums1.insert(j, nums2[i])
                        min = j+1
                        break
                    if nums2[i] >= nums1[len(nums1)-1]:
                        nums1.insert(len(nums1), nums2[i])
                        break
                    if nums2[i] >= nums1[j] and len(nums1)-j > 1 and nums2[i] <= nums1[j+1]:
                        nums1.insert(j+1, nums2[i])
                        min = j+1
                        break
        # ic(nums1)
        len_nums1 = len(nums1)
        if len_nums1 % 2 == 0:
            n = len_nums1 // 2
            return (nums1[n] + nums1[n-1]) / 2
        else:
            n = len_nums1 // 2
            return float(nums1[n])

ic(Solution().findMedianSortedArrays([1,3], [2]))
ic(Solution().findMedianSortedArrays([1,2], [3,4]))
ic(Solution().findMedianSortedArrays([], [1]))
ic(Solution().findMedianSortedArrays([3], [-2, -1]))
