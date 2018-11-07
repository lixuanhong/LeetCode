"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

"""

“”“
思路：图形学, 对startlist和endlist排序，比较startlist[i]和endlist[endpointer]; 如果startlist[i]在endlist[endpointer]前开始会议，那么需要增加
会议室；如果startlist[i]在endlist[endpointer]之后，那么说明前面的会议室空出来可以用，endpointer向后移一位

start:
| |   |

end:
    |   |   |


”“”

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)                #这里用start, end是因为题目给定了interval的数据结构
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        res = 0
        idx = 0
        for i in range(len(intervals)):
            if start[i] < end[idx]:  #注意：这里比较的是endpointer, 容易写错成为i
                res += 1
            else:
                idx += 1
        return res
