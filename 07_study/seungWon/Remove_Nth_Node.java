/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int len = 0;

        ListNode tmp = head;
        ListNode next;
        ListNode prev;
        List<ListNode> storage = new ArrayList<ListNode>();
        
        if(head.next == null){
            return null;
        }
        
        //일단 다 넣고
        while(tmp!=null){
            storage.add(tmp);
            tmp = tmp.next;
        }
        
        // 특정아이를 빼고
        len = storage.size();
        storage.remove(len-n);
        len = storage.size();
        
        // 다시 링크드를 만듦 
        head = storage.get(0);
        head.next = null;
        prev = head;
        
        for(int i=len-1; i>0; i--) {
            prev = head.next;
            next = storage.get(i);
            next.next = prev;
            head.next = next;
        }
        
        return head;
    }
}
