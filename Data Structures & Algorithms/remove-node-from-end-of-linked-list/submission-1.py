# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            return None
        
        curr = head
        count = 1
        while curr.next:
            if count == n:
                temp = curr.next
                curr.next = temp.next
                temp.next = None
                break
            curr = curr.next
            count += 1
        return head
