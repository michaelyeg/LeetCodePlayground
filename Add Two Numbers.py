# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
from typing import Optional
from icecream import ic


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toArray(self, carry=None):
        if carry is None:
            carry = []
        if self.next != None:
            carry.append(self.val)
            self.next.toArray(carry)
        else:
            carry.append(self.val)
        return carry


class Solution:
    # [2,4,3] => 342
    def getNumFromLN(self, ln: [ListNode]) -> int:
        if ln.next == None:
            return ln.val
        num = 0
        time = 0
        while ln.next != None:
            num += ln.val * (10 ** time)
            time += 1
            ln = ln.next
        # Additional iteration for the last node
        num += ln.val * (10 ** time)
        return num

    # 342 => [2,4,3]
    def getLNFromNum(self, num: int) -> ListNode:
        # Catch edge case of 0
        if num == 0:
            return ListNode(0)
        # First figure out how many digits the num have
        x = 1
        # How many digits num have
        n = 0

        while num // x != 0:
            x *= 10
            n += 1

        # In case of num = 0, consider as 1 digit
        # if n == 0:
        #     n += 1
        # Start with 1st digit, last node
        n -= 1
        last = num // (10 ** n)
        ln_all = ListNode(last)
        ln_last = ln_all
        # Storage for the remainder of num, e.g. 342 -> 42
        temp = num - last * (10 ** n)
        while n != 0:
            n -= 1
            last = temp // (10 ** n)
            ln_all = ListNode(last, ln_last)
            ln_last = ln_all
            temp = temp - last * (10 ** n)
        return ln_all

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = self.getNumFromLN(l1)
        l2_num = self.getNumFromLN(l2)
        sum_num = l1_num + l2_num
        return self.getLNFromNum(sum_num)


l1 = ListNode(0)
l2 = ListNode(0)
test = Solution()
ic(test.addTwoNumbers(l1, l2).toArray())
