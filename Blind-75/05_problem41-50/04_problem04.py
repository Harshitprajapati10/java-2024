# problem 44
# Reorder linked list
# LC 143
# 1,2,3,4,5,6,7
# 1,7,2,6,3,5,4


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def createLinkedList(self,nums):
        if not nums:  
            return None    
        head = ListNode(nums[0]) 
        current = head   
        for value in nums[1:]:  
            current.next = ListNode(value)  
            current = current.next  
        return head  

    def ShowLinkedList(self,head):
        temp = head
        while(temp is not None):
            print(temp.val, end=" -> " if temp.next else "\n")
            temp = temp.next
    
    def reorder_linked_list(self, head):
        slow, fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # merge
        first,second = head, prev
        while second:
            tmp1, tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head


obj = Solution()
head = obj.createLinkedList([1,2,3,4,5,6,7])
obj.ShowLinkedList(head)

mid = obj.reorder_linked_list(head)
obj.ShowLinkedList(mid)