# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
two pointers 
store values in an ordered set
[1,2,3,4]
   s
   e
 1->2->3->4
          *
 *
 1->4->2->3

 1->2->3->4->5
 *
       *      

1->2
     *
5->4->3
      *

1->5->2->4->3
 find the midpoint
 reverse a linked list
 merge two lists

'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        slow = head
        fast = head
        while fast is not None:
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            
        mid = slow
        prev = None
        curr = mid
        nex = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            if nex is not None:
                nex = nex.next
        
        curr = head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        
        list1 = head.next
        list2 = prev
        
        curr = head
        swapbool = False
        while list1 is not None or list2 is not None:
            if swapbool:
                curr.next = list1
                list1 = list1.next
            elif not swapbool:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

            swapbool = not swapbool