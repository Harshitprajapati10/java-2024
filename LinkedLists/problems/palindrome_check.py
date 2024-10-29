#234 -> palindrome check of linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def createLinkedList(self, nums):
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


    def getSize(self,head):
        size = 0
        temp = head
        while(temp is not None):
            temp = temp.next
            size += 1
        return size

    def reverseList(self,head):
        if self.getSize(head) < 2:
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

    def getMid(self,head):
        s = head
        f = head
        while(f!=None and f.next!=None):
            s = s.next
            f = f.next.next
        return s

    def isPalindrome(self,head):
        mid = self.getMid(head)
        head_second = self.reverseList(mid)
        reReverseHead = head_second
        
        while head!=None and head_second!=None:
            #check both halves
            if head.val != head_second.val:
                break
            head = head.next
            head_second = head_second.next
        self.reverseList(reReverseHead) 
        return head == None or head_second == None

def main():
    obj = solution()
    head = obj.createLinkedList([1,2,3,4,5,4,3,2,1])
    obj.ShowLinkedList(head)
    print(obj.isPalindrome(head))
    obj.ShowLinkedList(head)

# find mid using fast and slow pointer 
# reverse mid till end
# compare both things, rereverse mid till end to get og Linked list

if __name__ == "__main__":
    main()