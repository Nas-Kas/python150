'''
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

use a priority queue to sort the values by their frequency
what is a priority queue in python?

- traverse through nums
- while traversing through nums create a frequency map
- put the values from that map into a priority queue
- use a while loop to traverse the priority queue
- pop off values until you have k values in a result list

[4,1,-1,2,-1,2,3]
fMap[]

There a three different types of priority queues in python 
class based priority queue from the queue library
probably the best option*

'''

from typing import List
from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        pq = PriorityQueue()
        res = []
        for x in nums:
            if x in freqMap:
                freqMap[x] += 1
            else:
                freqMap[x] = 1

        for x in freqMap:
            pq.put((-freqMap[x], x))
        for x in range(k):
            res.append(pq.get()[1])
        return res
    
    '''
    using an array as a priority queue
    customers = []
    customers.append([2,"harry"])
    customers.append([3,"charles"])
    customer.append([1,"riya"])
    customers.append([4,"stacy"])
    customers.sort(reverse=True)
    customers should come out in reverse order based on the first value
    i.e when you pop it should look like
    [stacy,charles,harry,riya] -> because we are sorting by the key in this tuple
    sort by default sorts by the first value in the array
    '''

    def topKFrequentArrSoln(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        pq = []
        res = []
        for x in nums:
            if x in freqMap:
                freqMap[x] += 1
            else:
                freqMap[x] = 1
        for x in freqMap:
            pq.append([[freqMap[x]],x])
        pq.sort()
        while k > 0:
            res.append(pq.pop()[1])
            k -= 1
        return res
    
'''
- heapq is a built in heap that only has a min heap implementation
    its absolutely garbage unless you're using a min heap but this can be converted into a maxheap using a custom comparator import heapq
    - you can also just make the priority values negative when you insert them instead
    # Custom comparison function for max heap
    def max_heapify(x):
        return -x

    # Original min heap
    min_heap = [1, 3, 5, 7, 9]

    # Turn heapq into a max heap using custom comparison function
    max_heap = []
    for item in min_heap:
        heapq.heappush(max_heap, max_heapify(item))

    print(max_heap)  # Output: [9, 7, 5, 1, 3]
    DOESNT WORK FIGURE OUT HOW TO FIX THIS GARBAGE LIBRARY HEAPQ DISASTER BULLSHIT
'''
    # def comparator(self, x):
    #     return -x[0]

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freqMap = {}
    #     pq = []
    #     res = []
    #     for x in nums:
    #         if x in freqMap:
    #             freqMap[x] += 1
    #         else:
    #             freqMap[x] = 1
    #     for x in freqMap:
    #         heapq.heappush(pq, (freqMap[x], x))
    #     while k > 0:
    #         val = heapq.heappop(pq)
    #         res.append(val[0])
    #         k -= 1
    #     return res