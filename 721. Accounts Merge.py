"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

"""
并查集+路径压缩
Union-Find 经典题目

"""

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        eset = set()
        owner = {}
        parent = {}
        result = collections.defaultdict(list) #当字典的value是一个list时，直接用collections.defaultdict很灵活！！
        def findParent(e):
            rank = 0
            while parent[e] != e:
                rank += 1
                e = parent[e]
            return e, rank

        def merge(a, b):
            pa, ra = findParent(a)
            pb, rb = findParent(b)
            if ra < rb: parent[pa] = pb
            else: parent[pb] = pa

        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                eset.add(email)
                owner[email] = name
                if email not in parent:
                    parent[email] = email
            for email in emails[1:]:
                merge(emails[0], email)

        for email in eset:
            result[findParent(email)[0]].append(email)
        return [[owner[k]] + sorted(v) for k, v in result.iteritems()] #注意：collections.defaultdict不能用items()要用iteritems()

"""
为什么[owner[k]] + sorted(v)? 两个list相加，才能合并

a = ["John"]

b = [1, 2, 3]

print(a+b) => ['John', 1, 2, 3]

"""
