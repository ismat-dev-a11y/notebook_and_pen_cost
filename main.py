# leetcode 1-masala
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index
# leetcode 2-masala
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            carry, sum_val = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(sum_val)
        
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
# leetcode 3 - masala
