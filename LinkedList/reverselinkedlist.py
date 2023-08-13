# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''

 <-1<-2<-3<-4<-5
               p
                  c
                  n
create prev curr and nex pointer

repeat these steps until curr is equal to null
currs next is equal to previous
prev is equal to curr
curr is equal to nex

if nex is not null
nex is equal to nex.next

return prev

Questions
a single node is considered reversed?
will nodes only contain integers?
should this be recursive or iterative
is there a time complexity we are aiming for?

5 mins
7 mins
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        prev = None
        curr = head
        nex = head.next
        while curr != None:
            curr.next = prev
            prev = curr
            curr = nex
            if nex != None:
                nex = nex.next
        return prev
