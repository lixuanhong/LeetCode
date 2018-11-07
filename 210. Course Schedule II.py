"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graphMap = collections.defaultdict(list)
        for prerequisite in prerequisites:
            if prerequisite[0] not in graphMap:
                graphMap[prerequisite[0]] = [prerequisite[1]]    #注意：这里是list，要加[]
            graphMap[prerequisite[0]].append(prerequisite[1])

        res = []
        visited = [[0] for i in range(numCourses)]

        //status: 0 - unknown 1 - visiting 2 - visited
        def dfs(cur, graphMap, visited, res):
            if visited[cur] == 1:
                return True                                 #有环
            if visited[cur] == 2:
                return False                                #没环

            visited[cur] = 1                                #首先开始visiting cur
            if cur in graphMap.keys():
                for next in graphMap.get(cur):
                    if dfs(next, graphMap, visited, res):
                        return True

            visited[cur] = 2
            visited.append(cur)                            #必须在这里append不能在前面的if里面append, 否则不能返回结果
            return False

        for i in range(numCourses):
            if dfs(i, graphMap, visited, res):
                return []
        return res
