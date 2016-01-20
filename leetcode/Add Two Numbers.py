# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        return self._addTwoSingleNumbers(l1, l2, 0)
 
    def _addTwoSingleNumbers(self, l1, l2, carry):
        value = carry
 
        # Make sure, either both l1 and l2 are None,
        #            or l2 is not None.
        # To simplify the if-elif block
        if l2 == None:      l1, l2 = l2, l1
 
        if l1 == None and l2 == None:
            if value == 0:  return None             # No need to create a new node
            else:           return ListNode(value)  # Create the last node
        elif l1 == None:
            # l2 is not None
            value += l2.val
            tempNode = ListNode(value % 10)
            tempNode.next = self._addTwoSingleNumbers(None, l2.next, value/10)
            return tempNode
        else:
            # Both are not None
            value += l1.val + l2.val
            tempNode = ListNode(value % 10)
            tempNode.next = self._addTwoSingleNumbers(l1.next, l2.next, value/10)
            return tempNode
