/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode(int x) : val(x), next(NULL) {}
* };
*/
class Solution {
public:
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		vector<ListNode*> nodeVector;
		map<int, ListNode*>::iterator iter;

		ListNode* node = head;

		while (node != NULL)
		{
			nodeVector.push_back(node);
			node = node->next;
		}

		int count = nodeVector.size();

		if (n == count)
		{
			head = head->next;
			return head;
		}
		else if (n == 0)
		{
			return head;
		}
		else if (n == 1)
		{
			nodeVector.at(count - 2)->next = NULL;
		}
		else
		{
			nodeVector.at(count - n) = NULL;
			nodeVector.at(count - n - 1)->next = nodeVector.at(count - n + 1);
		}

		return head;

	}
};