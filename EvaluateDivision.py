"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

"""
思路：graph + DFS  Time Complexity: O(e + q*e) Space Complexity: O(e)
https://www.youtube.com/watch?v=UwpvInpgFmo
"""

import collections
class Solution(object):
    def calEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):     #构图
            graph[x][y] = value
            graph[y][x] = 1.0 / value

        res = []
        for query in queries:
            x, y = query[0], query[1]
            if x not in graph or y not in graph:
                res.append(-1.0)
                continue
            visited = set()
            res.append(self.dfs(x, y, graph, visited))
        return res

    def dfs(self, x, y, graph, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for key in graph[x].keys():
            if key in visited:
                continue
            d = self.dfs(key, y, graph, visited)        #d = key/y
            if d > 0:                                   #x/y = key/y * x/key
                return d * graph[x][key]
        return -1.0
