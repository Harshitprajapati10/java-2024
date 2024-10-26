# 203 -> Remove linked list elements

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(nums):
    if not nums:  
        return None    
    head = ListNode(nums[0]) 
    current = head   
    for value in nums[1:]:  
        current.next = ListNode(value)  
        current = current.next  
    return head  

def ShowLinkedList(head):
    temp = head
    while(temp is not None):
        print(temp.val, end=" -> " if temp.next else "\n")
        temp = temp.next

def removeElements(head, value): # remove any specific element of Linked List
    while head is not None and head.val == value:
        head = head.next
    prev = None
    curr = head
    while(curr is not None):
        if curr.val == value:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head

head = createLinkedList([1,2,6,3,4,5,6])
# head = createLinkedList([7,7,7,7])
ShowLinkedList(head)
head = removeElements(head,6)
ShowLinkedList(head)



"""
[       1,  2,  6,  3,  4,  5,  6   ]
prev   curr                            if curr.val == tar -> prev.next = curr.next 
                                          curr = curr.next.next
"""