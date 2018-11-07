"""
Given the head of a graph, return a deep copy (clone) of the graph. Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. There is an edge between the given node and each of the nodes in its neighbors.


OJ's undirected graph serialization (so you can understand error output):
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.


As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.


Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
Note: The information about the tree serialization is only meant so that you can understand error output if you get a wrong answer. You don't need to understand the serialization to solve the problem.
"""

"""
思路：DFS
https://www.youtube.com/watch?v=V0j1IEBkK4k

https://blog.csdn.net/xyqzki/article/details/50347723
对于输入的graph， e.g. {0,1,2#1,2#2,2}, 这里可以看到1和2都不止出现了一次，所以不能在每次出现的时候都创建一个新的node。所以这里要用nodeMap做一个记录。
这里每个node的neighbors其实是表示一条边，不会表示重复的边。所以这里node 1 只有node 2这个neighbor.

用nodeMap {}来记录node和clone graph, key是需要复制的node, value是clone的graph; 注意undirectedGraphNode的数据结构(graph的基本组成数据结构)，
neighbors数组里面是相邻的每一个node, 这些node的neighbors(本身也是undirectedGraphNode)同样需要被复制，所以会用到DFS。

"""
class UndirectedGraphNode:
    def__init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        nodeMap = {}
        return self.helper(node, nodeMap)

    def helper(self, node, nodeMap):
        if node is None:
            return None
        if node in nodeMap.keys():
            return nodeMap.get(node)
        else:
            clone = UndirectedGraphNode(node.label)
            nodeMap[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(self.helper(neighbor, nodeMap))
        return clone
