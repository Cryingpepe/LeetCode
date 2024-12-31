/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode result = new ListNode();
        ListNode Final = result;
        boolean overTen = false;
        
        while (l1 != null || l2 != null){

            int sum = 0;

            if (overTen){
                sum = l1.val + l2.val + 1;
                result.val = sum % 10;
                overTen = false;
            }
            else{
                sum = l1.val + l2.val;
                result.val = sum % 10;
            }

            if (sum >= 10){
                overTen = true;
            }

            if (l1.next == null && l2.next != null){
                l1.next = new ListNode(0);
            }
            else if (l2.next == null && l1.next != null){
                l2.next = new ListNode(0);
            }
            else if (l1.next == null && l2.next == null && overTen){
                l1.next = new ListNode(0);
                l2.next = new ListNode(0);
            }
            
            if (l1.next != null && l2.next != null){
                l1 = l1.next;
                l2 = l2.next;
                result.next = new ListNode();
                result = result.next;
            }
            else{
                l1 = l1.next;
                l2 = l2.next;
            }
            
        }

        return Final;
    }
}