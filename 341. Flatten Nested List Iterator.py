"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
思路：利用栈（Stack）数据结构对嵌套列表展开，在hasNext方法内将下一个需要访问的整数元素准备好。递归一般都需用栈来辅助遍历，由于栈的后进先出的特性，
我们在对向量遍历的时候，从后往前把对象压入栈中，那么第一个对象最后压入栈就会第一个取出来处理，我们的hasNext()函数需要遍历栈，并进行处理，如果栈顶元素是整数，
直接返回true，如果不是（也就是说是个嵌套的list），那么移除栈顶元素，并开始遍历这个取出的list，还是从后往前压入栈，循环停止条件是栈为空，返回false.
https://blog.csdn.net/maymay_/article/details/80162847

例子：[1,[4,[6]]]
第一次反序压栈：[[4,[6]], 1]
第二次反序压栈：[[6], 4]

"""

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [n for n in reversed(nestedList)]  #反序压入栈，使第一个元素在栈顶


    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()       #是整数的时候pop出栈


    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:                          #栈不为空的时候执行下面程序
            top = self.stack[-1]                   #取栈顶
            if top.isInteger():                    #当栈顶是整数的时候
                return True                        #返回true, 然后执行next程序
            top = self.stack.pop()                 #如果栈顶不是整数，而是列表类型
            for n in reversed(top.getList()):      #又将列表反序压栈
                self.stack.append(n)
        return False



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
