/**
* Definition for binary tree
* struct TreeNode {
*     int val;
*     TreeNode *left;
*     TreeNode *right;
*     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
* };
*/
class BSTIterator {
public:
	BSTIterator(TreeNode *root) {
		index = 0;

		if (root != NULL)
		{
			InOrder(root);
		}
	}

	vector<int> valVector;
	int index;

	/** @return whether we have a next smallest number */
	bool hasNext() {
		return (index < valVector.size());
	}

	/** @return the next smallest number */
	int next() {
		return valVector[index++];
	}

	bool InOrder(TreeNode* node)
	{
		if (node->left != NULL)
		{
			InOrder(node->left);
		}

		valVector.push_back(node->val);

		if (node->right != NULL)
		{
			InOrder(node->right);
		}
	}

};

/**
* Your BSTIterator will be called like this:
* BSTIterator i = BSTIterator(root);
* while (i.hasNext()) cout << i.next();
*/