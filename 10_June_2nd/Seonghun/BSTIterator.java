/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
// step 1 : 
    // if there is left child, find smallest node in the left sub-tree, print the value of the node and do step 2.
    // if not, print current node and do step 2.


// step 2 : 
    // if there is right child, do step 1 with the right child node as a root of the sub-tree
    // if not, pop node from stack, print value of the node and do step 2 for the node

public class BSTIterator {
    
    private Stack<TreeNode> stack;
    private TreeNode thisNode;
    private int toDoStep;

    public BSTIterator(TreeNode root) {
        this.stack = new Stack();
        this.thisNode = root;
        this.toDoStep = 1;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        
        if (thisNode == null || toDoStep == 2 && thisNode.right == null && stack.isEmpty()) {
            return false;
        } 
        return true;
    }

    /** @return the next smallest number */
    public int next() {
        if (this.toDoStep == 1) {
            return doStep1(thisNode);
        } else {
            return doStep2();
        }
    }
    
    private int doStep1(TreeNode root) {
        
        this.toDoStep = 2;
        if (root.left != null) {
            TreeNode temp = root;
            while(temp.left != null) {
                stack.push(temp);
                temp = temp.left;
            }
            
            thisNode = temp;
            return temp.val;
        } else {
            thisNode = root;
            return root.val;
        }
    }
    
    private int doStep2() {
        
        if (thisNode.right != null) {
            return doStep1(thisNode.right);
        } else {
            thisNode = stack.pop();
            return thisNode.val;
        }
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */