# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None or (head.next is None and head.val==val ):
            return None
        elif head is None and head.val!=val:
            return head
        prev = None
        current = head
        while current:
            if head.val == val:
                head = head.next
            elif current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return head
        
        