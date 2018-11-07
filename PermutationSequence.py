"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""

"""
http://bangbingsyb.blogspot.com/2014/11/leetcode-permutation-sequence.html
1234
1243
1324
1342
1423
1432
2134
2143
2314  <= k = 9
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321

最高位可以取{1, 2, 3, 4}，而每个数重复3! = 6次。所以第k=9个permutation的s[0]为{1, 2, 3, 4}中的第9/6+1 = 2个数字s[0] = 2。

而对于以2开头的6个数字而言，k = 9是其中的第k' = 9%(3!) = 3个。而剩下的数字{1, 3, 4}的重复周期为2! = 2次。所以s[1]为{1, 3, 4}中的第k'/(2!)+1 = 2个，即s[1] = 3。

对于以23开头的2个数字而言，k = 9是其中的第k'' = k'%(2!) = 1个。剩下的数字{1, 4}的重复周期为1! = 1次。所以s[2] = 1.

对于以231开头的一个数字而言，k = 9是其中的第k''' = k''/(1!)+1 = 1个。s[3] = 4
"""

class Solution:
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        fac = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fac[i] = fac[i-1] * i
        for i in range(n, 0, -1):
            first = k // fac[i-1]
            k %= fac[i-1]
            res += num[first]
            num.pop(first)
        return res



# My Solution - 这里用dfs超时，如果是java或者c++用dfs可以通过
class Solution(object):
    def getPermutation(self, n, k):
        def Permutation(arr, tmp, res):
            if len(tmp) == n:
                res.append(tmp)
            for i in range(len(arr)):
                if str(arr[i]) in tmp:  #string里面没有append和pop, 要注意arr[i]是int, 要转换成str. 这个判断很重要，如果已经有了，要跳出当前循环，继续下一次！！
                    continue
                tmp += str(arr[i])
                Permutation(arr, tmp, res)
                tmp = tmp[:-1]   #取了tmp的substring要重新赋值给tmp
            return res
        arr = [i+1 for i in range(n)]
        res = []
        Permutation(arr, "", res)
        return res[k-1]

obj = Solution()
print(obj.getPermutation(3, 3))
