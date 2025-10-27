# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        left, right = head, head.next

        while right and right.next:
            left = left.next
            right = right.next.next

        mid = left.next
        left.next = None

        leftLink = self.sortList(head)
        rightLink = self.sortList(mid)

        def merge(left, right):

            start = ListNode()
            end = start

            while left and right:
                if left.val < right.val:
                    end.next = left
                    left = left.next
                else:
                    end.next = right
                    right = right.next

                end = end.next

            if left:
                end.next = left
            else:
                end.next = right

            return start.next
            

        return merge(leftLink, rightLink)
