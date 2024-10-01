public class ListNode{
    int val;
    ListNode next;
    ListNode() {
    }
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    //remove nth from the end
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
            return null;
        }  
        ListNode temp = head;
        int size = 0;
        while (temp != null) {
            temp = temp.next;
            size++;
        }
        if (n == size) {
            return head.next;
        }
        ListNode temp1 = head;
        int to_traverse = size - n - 1;
        while (to_traverse > 0) {
            temp1 = temp1.next;
            to_traverse--;
        }
        temp1.next = temp1.next.next;   
        return head;
    }
}