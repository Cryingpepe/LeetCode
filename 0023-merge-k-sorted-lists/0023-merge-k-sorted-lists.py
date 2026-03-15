# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            result = []

            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i + 1] if i + 1 < len(lists) else None
                result.append(self.merge_lists(left, right))

            lists = result

        return lists[0]

    def merge_lists(self, left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val > right.val:
                current.next = right
                right = right.next
            else:
                current.next = left
                left = left.next

            current = current.next

        if left:
            current.next = left
        else:
            current.next = right

        return dummy.next