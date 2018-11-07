"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

"""

“”“
Time O(N)
Space O(1)
先统计数组中各个任务出现的次数。优先安排次数最多的任务。次数最多的任务安排完成之后所需的时间间隔为（max(次数)-1）*（n+1）+ p(频率最高出现的p个数p>=1)。其余任务直接插空即可。
https://www.youtube.com/watch?v=YCD_iYxyXoo
特殊情况：如果不需要插入任何idle就能把所有task安排完，那么返回的就是task的长度
””“

class Solution(object):
    def leastInterval(self, tasks, n):
        counts = [0] * 26
        p = 0
        for i in tasks:
            counts[ord(i) - ord('A')] += 1
        max_count = max(counts)
        for count in counts:
            if count == max_count:
                p += 1
        ans = (max_count - 1) * (n + 1) + p
        return max(ans, len(tasks))      #这里很容易犯错，要考虑不需要任何idle, 就可以满足的情况！！
