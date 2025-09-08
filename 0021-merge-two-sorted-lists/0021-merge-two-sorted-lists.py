# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result = ListNode()
        pointer = result


        while list1 or list2:
            if not list1 and list2:
                result.next = list2
                result = result.next
                list2 = list2.next
            elif not list2 and list1:
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    result.next = list2
                    result = result.next
                    list2 = list2.next
                else:
                    result.next = list1
                    result = result.next
                    list1 = list1.next
        
        return pointer.next
        


        