class MinStack {
    
    class Node{
        int num;
        int min_num;
    }
    
    LinkedList<Node> ll = new LinkedList<>();

    public void push(int x) {
        
        Node node = new Node();
        node.num = x;
        try{
            Node lastNode = ll.getLast();
		    if(lastNode.min_num > x){
			    node.min_num = x;
		    } else {
		        node.min_num = lastNode.min_num;
		    }
        } catch(Exception e){
            node.min_num = x;
        }
	
		ll.add(node);
	}

	public void pop() {
		ll.removeLast();
	}

	public int top() {
		return ll.getLast().num;
	}

	public int getMin() {
		return ll.getLast().min_num;
	}
}
