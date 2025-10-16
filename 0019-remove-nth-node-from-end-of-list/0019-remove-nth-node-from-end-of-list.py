# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        temp = head

        while temp:
            leng += 1
            temp = temp.next
        
        if leng == n:
            return head.next
        
        np = leng - n
        temp = head
        count = 1

        while count < np:
            temp = temp.next
            count += 1
        temp.next = temp.next.next

        return head

        