# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
		sentinelNode = ListNode(0)
		sentinelNode.next = head
		
		endNode = sentinelNode
		targetNode = sentinelNode
		
		for each in range(n) :
			endNode = endNode.next
			
		while endNode.next != None :
			endNode = endNode.next
			targetNode = targetNode.next
			
		targetNode.next = targetNode.next.next
		
		return sentinelNode.next