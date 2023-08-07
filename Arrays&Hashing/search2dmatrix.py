'''
search through each list using the first value in the array as the start value
and the last value as the end value
if the target is inbetween the first and end value do a binary search
otherwise move to the next array
if you get to the end and you cant find it or the range goes above the target
return false
13 mins
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            start = x[0]
            end = x[len(x) - 1]
            print(start)
            print(end)
            if target <= end and target >= start:
                print("bin")
                return self.binSearch(x,target)

        return False

    def binSearch(self, arr: List[int], target: int):
        start = 0
        end = len(arr) - 1
        mid = int(end / 2)
        while start <= end:
            mid = int(start + (end - start) / 2)
            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                return True
        return False