# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        i,j = 0, len(stack) - 1
        while i < j:
            stack[i].val, stack[j].val = stack[j].val, stack[i].val
            i += 1
            j -= 1
        
        return head