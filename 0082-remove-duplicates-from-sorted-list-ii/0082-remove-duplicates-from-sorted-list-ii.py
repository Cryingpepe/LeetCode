# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        isDup = False

        while curr.next:
            if curr.val == curr.next.val:
                isDup = True
                curr = curr.next

            else:
                if isDup:
                    prev.next = curr.next
                    isDup = False

                else:
                    prev = prev.next
                    
                curr = curr.next

        if isDup:
            prev.next = curr.next

        return dummy.next
