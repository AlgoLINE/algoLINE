import java.util.ArrayList;
import java.util.HashMap;

import single_num.Graph;
import single_num.Graph.Node;
import single_num.Graph.State;


class Graph<T> {

	HashMap<T, Node> graph = new HashMap<T, Node>();

	public enum State {
		Unvisited, Visited;
	}

	class Node<T> {

		T value;
		ArrayList<Node> nodes;
		State state;
		int visitCtn = 0;

		public Node(T value) {
			this.value = value;
			nodes = new ArrayList<Node>();
		}

		public Node(Node value) {
			nodes = new ArrayList<Node>();
			nodes.add(value);
			visitCtn++;

		}

		public void insertLink(Node node) {
			if (nodes != null) {
				nodes.add(node);
				visitCtn++;
			}
		}
		
		public Node getNode(int index){
			return nodes.get(index);
		}
	}

	public Node insertNode(T value) {
		if (graph.containsKey(value)) {
			return graph.get(value);
		} else {
			Node newNode = new Node(value);
			graph.put(value, newNode);
			return newNode;
		}
	}

	public void linkingNode(T source, T target) {
		Node sourceNode = insertNode(source);
		sourceNode.insertLink(insertNode(target));
	}
	
	
}

class DFS<T> {


	public DFS(Graph g, Node rootNode, T searchObject) {

		T value = searchValue(rootNode, searchObject);

		if (value != null) {
			System.out.println(value);
		} else {
			System.out.println("is not exist");
		}

	}

	public T searchValue(Node node, T searchObject) {

		if (searchObject.equals(node.value)) {
			return searchObject;
		} else {
			T value = null;
			switch (node.state) {
			case Unvisited:
				if (node.visitCtn > 0) {
					value = searchValue(node.getNode(--node.visitCtn), searchObject);
					
				} else{
					node.state = State.Visited;
				}
				return value;
				
			case Visited:
				return null;
			default:
				return null;
			}
		}
	}
