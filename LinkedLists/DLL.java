public class DLL {
    private Node head;

    private class Node{
        int val;
        Node next;
        Node prev;
        public Node(int val){
            this.val = val;
        }
        public Node(int val , Node next, Node prev){
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }

    public void insertFirst(int val){
        Node node = new Node(val);
        node.next = head;
        node.prev = null;
        if(head != null){
            head.prev = node;
        }
        head = node;
    }

    public void display(){
        Node node = head;
        Node last = null;
        while(node != null){
            System.out.print(node.val + "->");
            last = node;
            node = node.next;
        }
        System.out.println("END!");
        System.out.println("Print in reverse order");
        while(last!=null){
            System.out.print(last.val + "->");
            last = last.prev;
        }
        System.out.println("START!");
    }

    public void insertLast(int val){
        Node node = new Node(val);
        Node last = head;
        node.next = null;
        if(head == null){
            node.prev = null;
            head = node;
            return;
        }
        while (last.next != null) {
            last = last.next;
        }
        last.next = node;
        node.prev = last;
    }

    public Node find(int value){
        Node node = head;
        while (node != null) {
            if(node.val == value){
                return node;
            }
            node = node.next;
        }
        return null;
    }

    public void insert(int after, int val){ //insert after some value
        Node p = find(after);
        if(p==null){
            System.out.println("Does not exist");
            return;
        }
        Node node = new Node(val);
        node.next = p.next;
        p.next = node;
        node.prev = p;
        if(node.next != null){
            node.next.prev = node;
        }
    }

    public static void main(String[] args) {
        DLL dll = new DLL();

        dll.insertFirst(12);
        dll.insertFirst(2);
        dll.insertFirst(82);
        dll.insertFirst(94);
        dll.display();

        dll.insertLast(31);
        dll.insertLast(32);
        dll.insertLast(33);
        dll.display();

        dll.insert(82, 45);
        dll.display();
    }
}
