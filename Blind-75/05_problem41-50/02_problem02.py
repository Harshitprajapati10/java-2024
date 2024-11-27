# problem 42
# merge k linked lists
# lc 23

# [[1,4,5],[1,3,4],[2,6]]
# out: [1,1,2,3,4,4,5,6]

# [head1,head2,....headn] ---> return head of merged one


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

    def merge_k_linked_list(self, lists):
        if not lists or len(lists) == 0: return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(self.merge_two_linked_lists(l1,l2))
            lists = mergedLists
        return lists[0]
    
obj = Solution()
head1 = obj.createLinkedList([1,4,5])
head2 = obj.createLinkedList([1,3,4])
head3 = obj.createLinkedList([2,6])
res = obj.merge_k_linked_list([head1,head2,head3])
obj.ShowLinkedList(res)

