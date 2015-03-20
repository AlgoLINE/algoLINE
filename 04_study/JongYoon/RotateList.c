struct ListNode *rotateRight(struct ListNode *head, int k) {
    
    int count = 1;
    struct ListNode *currNode = head;
    struct ListNode *rotateNode = head;
    struct ListNode *temp;
    
    if(!head || k == 0){
        return head;
    }
    
    for(  ;count <= k ; count++){
        if(currNode->next) { currNode = currNode->next; }
        else{
            k = k % count;
            if(k == 0) return head;
            count = 0;
            currNode = head;
        }
    }
    
    while(currNode->next){
        currNode = currNode->next;
        rotateNode = rotateNode->next;
    }
    
    temp = rotateNode->next;
    currNode->next = head;
    rotateNode->next = 0;
    head = temp;
    
    return head;
}