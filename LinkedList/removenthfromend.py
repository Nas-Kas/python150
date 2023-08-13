# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

'''
nth node from end
- find the size of the list then find the nth behind from the list
- can do this using slow/fast pointers


if the value is at the front of the list
- set head to head.next

if the value is at the middle of the list
- use a prev pointer and set it to curr.next

if the value is at the end of the list
- set prev.next to none

Questions
will n ever be greater than the size of the list if so what do i do?
if n is zero i remove from head and reassign the new head
if n is lenght of the list i remove the tail

[1,2,3,4,5]
       s
           f
while n > 0
increment f and decrement n
while fast is not none
increment both slow and fast
when you're done slow will be pointing to the nth from the end node?
5 min

1 -> 2 -> 3 -> 4 -> 5
               c
          p    
                    
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = ListNode(-1)
        while n > 0:
            n -= 1
            fast = fast.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        if prev.val == -1: #if the value we want to remove is head
            head = head.next
        elif slow.next == None: # if the value we want to remove is tail
            prev.next = None
        else: # the value is somewhere in the middle
            prev.next = slow.next
            slow.next = None 
        return head 