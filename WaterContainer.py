"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""
class Solution(object):
    def maxArea(self, height):
        left = 0; right = len(height) - 1
        area = 0
        while left < right:
            water = (right - left) * min(height[left], height[right])
            if water > area: area = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
#用左右两个指针，不需要两个loop



# My Solution - Time Limit Exceed
class Solution(object):
    def maxArea(self, height):
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                tmp = (j-i) * min(height[i], height[j])
                area = max(area, tmp)
        return area

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))
