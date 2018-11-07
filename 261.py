"""
Graph Valid Tree

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

2 -- 0 -- 1 -- 4
     |
     3

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

     4
     |
0 -- 1 -- 2
      \  /
       3

time: O(edges * ndoes)
space: O(n)
"""

"""
思路：Union Find
判断一个图是不是一棵树①首先应该有n-1条边　②边没有形成环

初始端点n个是独立的, 并且每个端点的父结点为自身索引. 利用并查集, 如果一条边的两个端点的最终父结点不相同, 那么两个端点就可以合并到一个集合中. 最后看是否只有一个集合即可.

For each edge, make subsets using both the vertices of the edge. If both the vertices are in the same subset, a cycle is found.
https://www.youtube.com/watch?v=mHz-mx-8lJ8
"""


class Solution(object):
    def validTree(self, n, edges):
        if n != len(edges) + 1:
            return False

        root = [i for i in range(n)]
        for edge in edges:
            if self.find(root, edge[0]) == self.find(root, edge[1]):
                return False
            else:
                self.union(root, edge[0], edge[1])
        return True

    def find(self, root, e):
        if root[e] == e:
            return e
        return self.find(root, root[e])

    def union(self, root, x, y):
        xset = self.find(root, x)
        yset = self.find(root, y)
        root[xset] = yset
