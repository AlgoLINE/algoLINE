struct ListNode *insertionSortList(struct ListNode *head) {
    struct ListNode *iterator = head;
    struct ListNode *presentNode = head;
    struct ListNode *prevChangeNode = head;
    struct ListNode *prevPresentNode = head;
    int cycleFlag = 0;
    
    if (head == NULL) {
        return head;
    }
    
    if (head->next == NULL) {
        return head;
    }
    
    presentNode = head->next; //start from head's next node
    
    while (1) {
        
        while (iterator != presentNode) {
            if (iterator->val > presentNode->val) {
                if (iterator == head) {
                    head = presentNode;
                } else {
                    prevChangeNode->next = presentNode;
                }
                prevPresentNode->next = presentNode->next;
                presentNode->next = iterator;
                presentNode = prevPresentNode->next;
                cycleFlag = 1;
                break;
            }
            prevChangeNode = iterator;
            iterator = iterator->next;
            
        }
        
        if (presentNode == NULL && cycleFlag == 1) {
            break;
        }
        
        if (presentNode->next == NULL && cycleFlag == 0) {
            break;
        }
        
        if (cycleFlag == 0) { // don't swap
            prevPresentNode = presentNode;
            presentNode = presentNode->next;
        }
        iterator = head;
        prevChangeNode = head;
        cycleFlag = 0;
        
    }
    
    return head;
}