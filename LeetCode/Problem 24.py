# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        elif head.next == None:
            return head
        else:
            prev=  head
            curr = head.next
            while curr != None and curr.next != None :
                prev.val, curr.val = curr.val, prev.val
                prev = curr.next
                curr = prev.next

            if curr != None:
                prev.val, curr.val = curr.val, prev.val
            return head 

