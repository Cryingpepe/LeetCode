# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next: 
            return head
    
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:

            first = current.next
            sec = current.next.next

            current.next = sec
            first.next = sec.next
            sec.next = first
            
            current = current.next.next

        return dummy.next   