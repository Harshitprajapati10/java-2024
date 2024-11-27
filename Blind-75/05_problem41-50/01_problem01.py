# problem 41

# Merge two sorted linked lists
# LC 21
# head= 1,2,4, head2= 1,3,4
# output = 1,1,2,3,4,4

"""
head1 = 1 ,2, 4
        f
head2 = 1, 3, 4
        s
head = 1



head1 = 1 ,2, 4
           f
head2 = 1, 3, 4
        s
head = 1 ,1



head1 = 1 ,2, 4
           f
head2 = 1, 3, 4
           s
head = 1 ,1, 2



head1 = 1 ,2, 4
              f
head2 = 1, 3, 4
           s
head = 1 ,1, 2


head1 = 1 ,2, 4
              f
head2 = 1, 3, 4
              s
head = 1 ,1, 2,3


head1 = 1 ,2, 4
              f
head2 = 1, 3, 4
                 s
head = 1 ,1, 2,3,4



head1 = 1 ,2, 4
                 f
head2 = 1, 3, 4
                 s
head = 1 ,1, 2, 3, 4, 4
"""


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
    
    def merge_two_linked_lists(self, head1, head2):
        temp = ListNode()
        current = temp
        while(head1 and head2):
            if(head1.val <= head2.val):
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        if head1: current.next = head1
        elif head2: current.next = head2
        return temp.next


obj = Solution()
head1 = obj.createLinkedList([1,2,4,5,6,7,8])
obj.ShowLinkedList(head1)
head2 = obj.createLinkedList([1,3,4])
obj.ShowLinkedList(head2)

head = obj.merge_two_linked_lists(head1,head2)
obj.ShowLinkedList(head)