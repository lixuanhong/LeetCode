"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

"""
Eulerian path(欧拉路径) - an Eulerian trail is a trail in a finite graph which visits every edge exactly once 每个票用一次并且全部用掉
Hierholzer算法
path = []
DSF(u):
    while (u存在未被访问的边e（u,v))
        mark边(u,v)为访问
        DSF(v)
    END
    path.pushleft(u)
建图O(n+nlgn), Hierholzer: O(n) Estimated Time: O(n+nlgn+n) -> O(nlgn) Space:O(n)
"""

import collections
class Solution(object):
    def findItinerary(self, tickets):
        if not tickets:
            return []
        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for key in graph:
            graph[key].sort()
        res = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            res.append(start)                        #从后往前append
        dfs("JFK")
        return res[::-1]                             #所以最后需要返回倒序！





"""
根据题意，input是一系列换乘的机票，肯定有一种方式可以连接起来。要求从JFK出发，把所有的机场按照顺序排序，同时，如果有选择，机场的顺序需要按照字母顺序排列。

1. 采用字典，departure - [ arrival ]

2. dfs 深度搜索，递归调用

3. trace back 回溯，增加判断如果不可能的就恢复数据，然后返回继续dfs搜索
缺点：时间复杂度大 O(n) + O(nlgn) + O(n!)  Space: O(n)
"""

import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])                  #构图

        def dfs(start, res):
            if len(res) == len(tickets) + 1:
                return res

            cur = sorted(graph[start])                         #对graph[start]进行排序，依次递归
            for dst in cur:
                graph[start].remove(dst)
                res.append(dst)

                if dfs(dst, res):                              #如果dfs可以持续进行下去，返回res
                    return res
                else:                                          #否则backtracking, 恢复graph[start]
                    res.pop()
                    graph[start].append(dst)

        res = ["JFK"]
        dfs("JFK", res)
        return res
