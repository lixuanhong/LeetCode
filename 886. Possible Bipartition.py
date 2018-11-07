"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""

"""
这个题和785. Is Graph Bipartite一模一样的。同样使用dfs去做，需要把每个节点都当做起始节点去染色，这样判断是否有冲突。染色的方式是0-未染色，1-染了红色，-1代表染了蓝色。

时间复杂度是O(V + E)，空间复杂度是O(V + E).
"""

import collections
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)    #全部-1因为后面需要用到的index是从0开始的
            graph[dislike[1] - 1].append(dislike[0] - 1)
        color = [0] * N
        def dfs(i, color):                            #注意：如果是嵌套的方法，方法要在调用前定义！！
            color[i] = color
            for neighbor in graph[i]:           #这里是枚举邻居
                if color[neighbor] == color:
                    return False
                if color[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True

        for i in range(N):
            if color[i] == 0 and not dfs(i, 1):    # 0: unknown; 1: red; -1: blue
                return False
        return True
