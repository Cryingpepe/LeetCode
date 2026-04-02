# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lista = headA
        listb = headB

        while lista != listb:

            if lista:
                lista = lista.next  
            else:
                lista = headB

            if listb:
                listb = listb.next
            else:
                listb = headA
        
        return listb