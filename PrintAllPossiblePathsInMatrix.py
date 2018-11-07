class Solution(object):
    def uniquePath(self, grids):
        if not grids:
            return []
        m, n = len(grids), len(grids[0])
        res = []
        path = [0 for i in range(m+n-1)]        #初始化path
        self.dfs(grids, 0, 0, res, path, 0)
        return res

    def dfs(self, grids, i, j, res, path, idx): #用idx来帮助实现backtracking
        m, n = len(grids), len(grids[0])
        if i == m-1:
            for k in range(j, n):
                path[idx+k-j] = grids[i][k]
            res.append(path[:])                 #因为path是在不停变化，所以一定是append path的copy!!!
            return

        if j == n-1:
            for k in range(i, m):
                path[idx+k-i] = grids[k][j]
            res.append(path[:])
            return

        path[idx] = grids[i][j]
        self.dfs(grids, i+1, j, res, path, idx+1)
        self.dfs(grids, i, j+1, res, path, idx+1)

# obj = Solution()
# grids = [[1,2,3],
#         [4,5,6]]
# print(obj.uniquePath(grids))
