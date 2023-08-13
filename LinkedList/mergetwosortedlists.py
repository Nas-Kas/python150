# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
dummy nodes?
create 1 dummy list to merge into
while l1pointer and l2pointer are not None
check to see which one is the lower value
add that node to the head of dummy
move dummy forward
and move that pointer forward

when one list is finished
add the end of the list that isnt finished to dummy
return dummys head.next

list1 = [1,2,4]
                *
list2 = [1,3,4]
             *

dummy [0]->[1]->[1]->[2]->[3]->[4]->[4]
       *         *
finish 7 min
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,None)
        res = dummy
        itr = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                itr.next = list1
                list1 = list1.next
            else:
                itr.next = list2
                list2 = list2.next
            itr = itr.next
        
        if list1 is not None:
            itr.next = list1
        elif list2 is not None:
            itr.next = list2
        return res.next
