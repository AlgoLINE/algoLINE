/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode insertionSortList(ListNode head) {
        if(head == null || head.next == null)   return head;
            
        ListNode cur = head.next, prv = head;
        while(cur != null){
            
            // find position
            ListNode find = head, prvFind = null;
            while(find.val < cur.val && find != cur){
                prvFind = find;
                find = find.next;
            }
            
            if(find == cur){
                cur = cur.next;
                prv = prv.next;
            }
            else{
                prv.next = cur.next;
                cur.next = find;
                if(find == head) head = cur; 
                else             prvFind.next = cur;
                cur = prv.next;
            }

        }
        
        return head;
        
    }
}
