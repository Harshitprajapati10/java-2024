# 2130 -> Twin sum in a linked list

# Reverse linked list from mid till end
# take two pointers in both halves and store sum in some variable
# return the maximum sum


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

    def pairSum(self, head):
        mid = self.getMid(head)
        head_second = self.reverseList(mid)
        reReverseHead = head_second

        max_sum_so_far = head.val + head_second.val
        
        while head!=None and head_second!=None:
            max_sum_so_far = max(max_sum_so_far, head.val + head_second.val)
            head = head.next
            head_second = head_second.next

        self.reverseList(reReverseHead) # restore the linked list
        return max_sum_so_far

def main():
    obj = solution()
    head = obj.createLinkedList([4,2,2,3,4,9,6,7,8,9,1,3])
    obj.ShowLinkedList(head)
    print(obj.pairSum(head))
    obj.ShowLinkedList(head)


if __name__ == "__main__":
    main()