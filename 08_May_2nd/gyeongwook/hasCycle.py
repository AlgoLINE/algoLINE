# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        step_one = head
        step_two = head
        
        while step_two is not None :
            step_one = step_one.next
            
            if step_two.next is not None :
                step_two = step_two.next.next
            else :
                break
            
            if step_one is step_two :
                return True
        
        return False