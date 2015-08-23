/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int max = 0;

    public int maxDepth(TreeNode root) {
        if(root == null)
            return 0;
        if(root.val == 0 && root.left == null && root.right == null)
            return 1;
            
        if(root.left != null)
            Iterator(root.left, 1);
        if(root.right != null)
            Iterator(root.right, 1);
        return max;
    }
    public void Iterator(TreeNode node, int level){
        if(node!=null){
            Iterator(node.left, ++level);
            if(level>max){
                max=level;
            }
            
            if(node.right!=null){
                Iterator(node.right, level);
            }
        }
    }
}
