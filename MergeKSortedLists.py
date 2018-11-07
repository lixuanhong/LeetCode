"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

"""
思路：用最小堆, 每个list有一个指针, k个指针放入堆中, 每次pop出最小的, 然后指向相应list的下一个node, 再push入堆。
这个算法每个元素要读取一次，即是k*n次，然后每次读取元素要把新元素插入堆中要logk的复杂度，所以总时间复杂度是O(nklogk)。空间复杂度是堆的大小，即为O(k)。
"""

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        minHeap = [(l.val, l) for l in lists if l]
        heapq.heapify(minHeap)                         #transform list x into a heap, in-place, in linear time

        head = cur = ListNode(0)

        while minHeap:
            pop = heapq.heappop(minHeap)           #pop and return the smallest item from the heap
            cur.next = pop[1]
            cur = cur.next

            if cur.next:
                heapq.heappush(minHeap, (cur.next.val, cur.next))   #push the value item onto the heap

        return head.next


#另外一种方法是merge linked list然后二分法递归; 时间复杂度O(nklgk), 空间复杂度O(lgK)
class Solution(object):
    def mergeKLists(self, lists):
        n = len(lists)
        if not lists or n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n = 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = n/2
            return self.mergeKLists([self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])])

    def mergeTwoLists(self, l1, l2):
        head = l = ListNode(0)
        while l1 and l2:
            if l1 <= l2:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        if not l1:
            l.next = l2
        else:
            l.next = l1
        return head.next
