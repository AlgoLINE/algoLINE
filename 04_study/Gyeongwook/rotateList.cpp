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
        if (head == nullptr || k == 0)
            return head;
            
        ListNode* curr = head;
        int listLen = 1;
        while (curr->next != nullptr) {
            ++listLen;
            curr = curr->next;
        }
        
        int rotateNum = k % listLen;
        if (rotateNum == 0)
            return head;
        
        int lastPos = listLen - rotateNum - 1;
        
        ListNode* lastNode = head;
        for (int i = 1; i <= lastPos; ++i) {
            lastNode = lastNode->next;
        }
    
        ListNode* startNode = lastNode->next;
        curr->next = head;
        lastNode->next = nullptr;
        
        return startNode;
    }
};