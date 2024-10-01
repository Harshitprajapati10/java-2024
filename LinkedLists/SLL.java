class SLL {
  private Node head;
  private Node tail;
  private int size;
  public SLL() {
    this.size = 0;
  }

  private class Node {
    private int value;
    private Node next;

    public Node(int value) {
      this.value = value;
    }

    public Node(int value, Node next) {
      this.value = value;
      this.next = next;
    }
  }

  // InsertFirst method
  public void insertFirst(int val) {
    Node node = new Node(val);
    node.next = head;
    head = node;
    if (tail == null) {
      tail = head;
    }
    size += 1;
  }

  // Display method
  public void display() {
    Node temp = head;
    while (temp != null) {
      System.out.print(temp.value + " -> ");
      temp = temp.next;
    }
    System.out.println("End!");
  }

  // Insert Last
  public void insertLast(int value) {
    if (tail == null) {
      insertFirst(value);
      return;
    }
    Node node = new Node(value);
    tail.next = node;
    tail = node;
    size ++;
  }

  //Insert at given index
  public void insert(int value, int index){
    if(index == 0){
      insertFirst(value);
      return;
    }
    if(index == size){
      insertLast(value);
      return;
    }
    Node temp = head;
    for (int i = 1; i < index; i++) {
      temp = temp.next;
    }
    Node node = new Node(value, temp.next);
    temp.next = node;
    size++;
  }


  //DeleteFirst
  public int deleteFirst(){
    int value = head.value;
    head = head.next;
    if(head == null){
      tail = null;
    }
    size --;
    return value;
  }

  //deleteLast
  public int deleteLast(){
    if(size <= 1){
      deleteFirst();
    }
    Node secondLast = get(size-2);
    int val = tail.value;
    tail = secondLast;
    tail.next = null;
    return val;
  }
  public Node get(int index){
    Node node = head;
    for (int i = 0; i < index; i++) {
      node = node.next;
    }
    return node;
  }


  // Deletion from particular index
  public int delete(int index){
    if(index == 0){
      return deleteFirst();
    }
    if(index == size-1){
      return deleteLast();
    }
    Node prev = get(index-1);
    int val = prev.next.value;
    prev.next = prev.next.next;
    return val;
  }

  // Finding a node by given value
  public Node find(int val){
    Node node = head;
    while(node != null){
      if(node.value ==  val){
        return node;
      }
      node = node.next;
    }
    return null;
  }


  //insertion using recursion
  public void insertRec(int val, int index){
    head = insertRec(val, index, head);
  }
  private Node insertRec(int val, int index, Node node){
      if(index == 0){
        Node temp = new Node(val, node);
        size++;
        return temp;
      }
      node.next = insertRec(val, index-1, node.next);
      return node;
  }

  // remove duplicates
  public void duplicates(){
    Node node = head;
    while(node.next != null){
      System.out.println(node.value);
      if(node.value == node.next.value){
        node.next = node.next.next;
        size--;
      }else{
        node = node.next;
      }
      tail = node;
      tail.next = null;
    }
  }


  //Merge sort
  public Node sortList(Node head){
    if(head == null || head.next == null){
      return head;
    }

    Node mid = getMid(head);
    Node left = sortList(head);
    Node right = sortList(mid);
    return merge(left,right);
  }
  public Node merge(Node list1, Node list2){
    Node dummy = new SLL().head;
    Node tail = dummy;
    while(list1 != null && list2 != null){
      if(list1.value < list2.value){
        tail.next = list1;
        list1 = list1.next;
        tail = tail.next;
      }else{
        tail.next = list2;
        list2 = list2.next;
        tail = tail.next;
      }
    }tail.next = (list1!=null)?list1:list2;
    return dummy.next;
  }
  public Node getMid(Node head){
    Node midPrev = null;
    while(head!=null && head.next != null){
      midPrev = (midPrev == null)?head:midPrev.next;
      head = head.next.next;
    }
    Node mid = midPrev.next;
    midPrev.next = null;
    return mid;
  }

  // addtiton of two LL

  /* 

    public ListNode addTwoNumbers(ListNode list1, ListNode list2) {
      ListNode f = list1, s = list2;
      ListNode ans = new ListNode(0); 
      ListNode dummy = ans;
      int carry = 0;
      while (f != null || s != null || carry != 0) {
          int sum = carry;
          if (f != null) {
              sum += f.val;
              f = f.next;
          }
          if (s != null) {
              sum += s.val;
              s = s.next;
          }
          dummy.next = new ListNode(sum % 10);
          carry = sum / 10;
          dummy = dummy.next;
      }
      return ans.next; 
  }

*/
  public static void main(String[] args) {
    SLL list = new SLL();
    list.insertFirst(4);
    list.insertFirst(4);
    list.insertFirst(2);
    list.insertFirst(1);
    list.insertFirst(1);
    list.insertFirst(1);
    list.display();
     
    // 1) Remove duplicates from singly linked list
    list.duplicates();
    list.display();
  }
}
