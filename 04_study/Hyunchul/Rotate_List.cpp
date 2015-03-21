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
	ListNode *rotateRight(ListNode *head, int k) {
		if (head == NULL) {
			return NULL;
		}

		if (head->next == NULL) {
			return head;
		}

		int count = 1;
		ListNode *last = head;
		ListNode *nextLast = head;

		while (last->next != NULL) {
			last = last->next;
			count++;
		}

		int nextLastIndex = count - (k % count) - 1;

		for (int i = 0; i < nextLastIndex; i++) {
			nextLast = nextLast->next;
		}

		last->next = head;
		head = nextLast->next;
		nextLast->next = NULL;

		return head;
	}
};