# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l=[]
        curr=head
        while curr:
            l.append(curr)
            curr=curr.next
        left,right=0,len(l)-1
        while left<right:
            l[left].next=l[right]
            left+=1
            if l[left]==l[right]:
                break
            l[right].next=l[left]
            right-=1
        l[left].next=None
        