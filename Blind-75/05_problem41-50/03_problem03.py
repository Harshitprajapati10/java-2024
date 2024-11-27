# problem 43
# remove nth from the end of the linked list
# LC : 19

# 1, 2,3,4 , n = 2

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
    
    def remove_nth_from_end(self, head, n):
        if n==0: return head
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head
        for _ in range(n): right = right.next
        while(right!=None):
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next

obj = Solution()
head = obj.createLinkedList([1,2,3,4,5,6,7])
obj.ShowLinkedList(head)

res = obj.remove_nth_from_end(head, 4)
obj.ShowLinkedList(res)