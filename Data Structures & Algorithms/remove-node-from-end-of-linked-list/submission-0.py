# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr:
            l.append(curr)
            curr=curr.next
        removeIndex=len(l)-n
        if removeIndex==0:
            return head.next
        l[removeIndex-1].next=l[removeIndex].next
        return head
