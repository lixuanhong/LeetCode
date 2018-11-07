"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""
#bottom-up
# class Solution:
#     def generate(self, numRows):
#         arr = []
#         for i in range(numRows):
#             arr.append([])
#         arr[0] =[1]
#         arr[1] = [1,1]
#         for i in range(1, len(arr)-1):
#             arr[i+1].append(1)
#             for j in range(len(arr[i])-1):
#                 arr[i+1].append(arr[i][j] + arr[i][j+1])
#             arr[i+1].append(1)
#
#         return arr

# obj = Solution()
# print(obj.generate(5))

#递归
class Solution:
    def generate(self, numRows):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        pre_res = self.generate(numRows - 1)
        last_item = pre_res[-1]
        new_last_item = [1]
        for j in range(len(last_item) - 1):
            new_last_item.append(last_item[j] + last_item[j+1])
        new_last_item.append(1)
        new_res = pre_res
        new_res.append(new_last_item)
        return new_res

obj = Solution()
print(obj.generate(5))
