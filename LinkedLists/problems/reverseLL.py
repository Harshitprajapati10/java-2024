# 206 -> Reverse the linked list 

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

def getSize(head):
    size = 0
    temp = head
    while(temp is not None):
        temp = temp.next
        size += 1
    return size

def reverseList(head):
    if getSize(head) < 2:
        return head
    prevVal = None
    presVal = head
    nextVal = presVal.next
    while(presVal is not None):
        presVal.next = prevVal
        prevVal = presVal
        presVal = nextVal
        if nextVal is not None:
            nextVal = nextVal.next
    head = prevVal
    return head


def main():
    head = createLinkedList([1,2,3,4,5,6,7,8,9])
    ShowLinkedList(head)
    head = reverseList(head)
    ShowLinkedList(head)

if __name__ == "__main__":
    main()