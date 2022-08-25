# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        zero = head
        if now.next is None:
            return
        now = now.next
        total = 0
        while(now):            
            if now.val != 0:
                total += now.val
                now = now.next
            else:
                now.val = total
                total = 0
                zero.next = now
                zero = now
                now = now.next
                
        return head.next 