# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        count = 1

        while head.next:
            head = head.next
            count += 1
        
        count -= n
        head = dummy.next

        if count == 0:
            return head.next

        while head.next:
            count -= 1

            if count == 0:
                head.next = head.next.next
                return dummy.next
            else:
                head = head.next


        

        