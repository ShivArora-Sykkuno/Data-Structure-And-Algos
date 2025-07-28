# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        face_value = 1
        num = 0
        temp =  l1
        while temp is not None:
            num = num + (temp.val * face_value)
            face_value = face_value * 10
            temp = temp.next
        temp =  l2
        face_value = 1
        while temp is not None:
            num = num + (temp.val * face_value)
            face_value = face_value * 10
            temp = temp.next
        
        # print(num)
        x = ListNode()
        temp = x
        while num != 0:
            insert = num % 10
            num //= 10
            temp.next = ListNode(insert)
            temp = temp.next



        if x.next is None:
            return x
        return x.next
        