"""Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed
to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0 """

# Best Solution
import collections
def fourSumCount(A,B,C,D):
    ab_sum = collections.Counter(a+b for a in A for b in B) # collections.Counter() dict subclass for counting hashable objects
    return sum(ab_sum[-c-d] for c in C for d in D)

"""
cnt = collections.Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(cnt)
Counter({'blue': 3, 'red': 2, 'green': 1})

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
     cnt[word] += 1
print(cnt)
Counter({'blue': 3, 'red': 2, 'green': 1})

"""

# Another Style
import collections
def fourSumCount(A,B,C,D):
    res = 0
    cnt = collections.defaultdict(int)
    for a in A:
        for b in B:
            cnt[a+b] += 1   # defaultdict(<class 'int'>, {-2: 2, 0: 2, 2: 0})

    for c in C:
        for d in D:
            res += cnt[-c-d]

    return cnt

"""
using int as argument, it makes the defaultdict useful for counting
s = 'mississippi'
d = defaultdict(int)
for k in s:
   d[k] += 1

d.items()
[('i', 4), ('p', 2), ('s', 4), ('m', 1)]

using list as argument, it is easy to group a sequence of key-value pairs into a dictionary of lists:
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

"""



# My Solution - Time Limit Excess
def fourSumCount(A, B, C, D):
    res, dict = 0, {}
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] + B[j] not in dict:
                dict[A[i] + B[j]] = [(i, j)]
            else:
                dict[A[i] + B[j]].append((i,j))

    for l in range(len(C)):
        for k in range(len(D)):
            T = -C[l] - D[k]
            if T in dict:
                for item in dict[T]:
                    res += 1
    return res

A = [ -1,-1]
B = [-1,1]
C = [-1, 1]
D = [ 1, -1]

print(fourSumCount(A,B,C,D))
