# problem 40
# Cycle detection in Linked list
# lc 141

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def has_cyclee(self, head):
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
