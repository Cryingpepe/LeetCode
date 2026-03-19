# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode(0, head)
        groupPrev = dummy
        curr = head

        for _ in range(length // k):
            groupStart = curr
            prev = None

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            groupPrev.next = prev
            groupStart.next = curr
            groupPrev = groupStart

        return dummy.next


        