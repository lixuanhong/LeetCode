"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

"""

# My Solution - O(N) 思路和merge intervals很像，注意要找最小相交的部分！！
class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort()
        stack = []
        for point in points:
            if not stack:
                stack.append(point)
                continue
            p = stack[-1]
            if point[0] <= p[1] <= point[1]:
               stack[-1] = [point[0], p[1]]
            elif point[0] <= p[1] and p[1] > point[1]:    #要找最小相交部分
               stack[-1] = [point[0], point[1]]
            else:
               stack.append(point)
        return len(stack)
