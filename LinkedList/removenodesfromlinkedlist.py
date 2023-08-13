# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
[1,2,3,4,5] -> [5]

[3,134,4,6,1,2] -> [134,6,2]

traverse array while values are ascending or are equal to?*
if value descends store the before value for later
otherwise keep incrementing

max = 13
mostrecentmax = 13

[13,8]
    *
https://leetcode.com/problems/remove-nodes-from-linked-list/description/

'''
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        temp = head
        maxArr = []
        dummy = ListNode(0)
        dummyhead = dummy
        while temp:
            res.append(temp.val)
            temp = temp.next
        res = res[::-1]
        maxVal = res[0]
        for x in res:
            if x >= maxVal:
                maxArr.append(x)
                maxVal = max(x,maxVal)
       
        maxArr = maxArr[::-1]
        #print(maxArr)

        for x in maxArr:
            dummy.next = ListNode(x)
            dummy = dummy.next

        return dummyhead.next