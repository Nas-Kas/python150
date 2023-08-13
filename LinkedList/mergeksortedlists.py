# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
merge two lists problem? but for each list in the list?
create a merge two lists function
loop over the lists for each value in the array and merge the lists together one by one

Question
will the list contain negative values?
will any of the lists in the lists of lists be empty
2 mins
14 mins
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        temp = lists[0]
        for x in range(1, len(lists)):
            temp = self.mergeTwoLists(temp,lists[x])

        return temp

    def mergeTwoLists(self, listA, listB):
        dummylist = ListNode(-1)
        head = dummylist
        while listA and listB:
            if listA.val > listB.val:
                head.next = listB
                listB = listB.next
            else:
                head.next = listA
                listA = listA.next
            head = head.next

        if listA:
            head.next = listA
        else:
            head.next = listB

        return dummylist.next
