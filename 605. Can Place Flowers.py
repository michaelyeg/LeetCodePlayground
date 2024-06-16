from typing import List
from icecream import ic

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        slot = 0
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                # Mark slot as non-empty to meet no two adjacent flowers
                flowerbed[i] = 1
                slot += 1

        return n <= slot


ic(Solution().canPlaceFlowers([1,0,0,0,1], 1))
ic(Solution().canPlaceFlowers([1,0,0,0,1], 2))
ic(Solution().canPlaceFlowers([1,0,0,0,0,1], 2))