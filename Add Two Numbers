# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addition = 0
        
        # create new List Node
        dummy = ListNode()
        current_node = dummy
        
        while l1 or l2 or addition:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            s = v1 + v2 + addition
            
            addition = s // 10
            n_new = s % 10
            
            print(v1,v2,addition)
            
            # add value to cur node
            current_node.next = ListNode(n_new)
        
            # move to next node
            current_node = current_node.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            
        return dummy.next
            
