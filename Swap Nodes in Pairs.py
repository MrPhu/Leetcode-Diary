# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def swapPairs(self, head: ListNode) -> ListNode:
        
        def recur_pairswap(sub_head):
            if sub_head is not None:
                sub_head.val, sub_head.next.val = sub_head.next.val, sub_head.val
                recur_pairswap(sub_head.next.next)
        
        recur_pairswap(head)   
        return head
