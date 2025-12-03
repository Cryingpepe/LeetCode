# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        count = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            count += 1
        
        k %= count
        if k == 0:
            return head
        
        tail.next = head
        
        steps = count - k
        newTail = head
        for _ in range(steps - 1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        
        return newHead


