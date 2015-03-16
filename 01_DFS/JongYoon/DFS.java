import single_num.Graph;
import single_num.Graph.Node;
import single_num.Graph.State;

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
