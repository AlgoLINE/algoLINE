/*Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
public class Solution {
    int sumPath = 0;
    boolean flag = false;
    
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null)
            return false;
            
        sumPath += root.val;
        
        if(sumPath==sum && root.left == null && root.right == null){
            return true;
        }
        
        if(root.left != null){
            
            flag = hasPathSum(root.left, sum);
        } 
        
        if(root.right != null) {
            flag = hasPathSum(root.right, sum);
        }
        
        
        if(flag) {
            return true;
        } else {
            sumPath -= root.val;
            return false;
        }
    }
}
