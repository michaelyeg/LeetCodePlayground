# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3599/
class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        num = []
        total_cost = 0
        for i in instructions:
            (less, more) = self.getInsertionCost(num, i)
            print((less, more))
            cost = min(less, more)
            total_cost += cost
            if cost == 0:
                num.append(i)
            else if less < more:
                num.insert(cost, i)
            else:
                num.insert(-cost, i)

        print (num)
        return total_cost

    def getInsertionCost(self, num, insert):
        less = 0
        more = 0
        for i in num:
            if (i < insert):
                less += 1
            if (i > insert):
                more = len(num) - num.index(i)
                break

        print('Insert ' + str(insert) + ' with cost min(' + str(less) + ', ' + str(more) + ')')
        result = (less, more)
        return result

sol = Solution()
# sol.createSortedArray([1,5,6,2])
sol.createSortedArray([1,2,3,6,5,4])