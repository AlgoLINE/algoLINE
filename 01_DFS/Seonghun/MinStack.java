class MinStack {
    
    class Node {
        public Node next = null;
        public Node back = null;
        public Node nextMin = null;
        public int value;
    }
    
    private Node head = null;
    private Node bottom = null;
    private Node minHead = null;
    
    public void push(int x) {
        
        if(head == null){
            head = new Node();
            head.value = x;
            bottom = head;
            minHead = head;
        }
        else{
            Node newNode = new Node();
            newNode.value = x;
            newNode.next = head;
            head.back = newNode;
            head = newNode;
            
            if(head.value <= minHead.value){
                head.nextMin = minHead;
                minHead = head;
            }
        }
        
    }

    public void pop() {
        
        int headValue = head.value;
        Node old = head;
        head = old.next;
        if(head != null)
            head.back = null;
        old = null;
        
        if(minHead.value == headValue){
            if(minHead.nextMin != null){
                minHead = minHead.nextMin;
            }
            else{
                minHead = bottom;
                Node node = bottom.back;
                while(node != null){
                    if(node.value <= minHead.value){
                        node.nextMin = minHead;
                        minHead = node;
                    }
                    node = node.back;
                }
            }
        }
    }

    public int top() {
        return head.value;
    }

    public int getMin() {
        
        return minHead.value;
        
    }
}
