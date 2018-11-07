"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graphMap = {}
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prerequisite = prerequisites[i][1]
            if course not in graphMap.keys():
                graphMap[course] = []
            graphMap.get(course).append(prerequisite)

        visited = [[] for i in range(numCourses)]
        for i in range(numCourses):
            if self.dfs(i, graph, visited):       #dfs返回true表示有环，false表示没环
                return False
        return True


    //states: 0 = unknown, 1 = visiting, 2 = visited
    def dfs(self, cur, graphMap, visited):
        if visited[cur] == 1:
            return True
        if visited[cur] == 2:
            return False

        visited[cur] = 1
        if cur in graphMap.keys():
            for next in graphMap.get(cur):
                if self.dfs(next, graphMap, visited):
                    return True

        visited[cur] = 2
        return False;
