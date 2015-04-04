# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        part1 = []
        part2 = []
        
        currentNode = head
        returnValue = head

        while currentNode is not None :
            nextNode = currentNode.next

            if len(part2) == 0 or currentNode.val <= part1[-1].val :
                while len(part1) is not 0 and currentNode.val < part1[-1].val :
                    part2.append(part1.pop())
            else :
                while len(part2) is not 0 and currentNode.val > part2[-1].val :
                    part1.append(part2.pop())
            
            if len(part1) is not 0 :
                part1[-1].next = currentNode
            else :
                returnValue = currentNode
            
            part1.append(currentNode);
            
            if len(part2) is not 0 :
                currentNode.next = part2[-1]
            else :
                currentNode.next = None
                
            currentNode = nextNode;
            
        return returnValue;