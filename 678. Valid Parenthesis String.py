"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""

"""
这里维护了两个变量low和high，其中low表示在有左括号的情况下，将星号当作右括号时左括号的个数(这样做的原因是尽量不多增加右括号的个数)，而high表示将星号当作左括号时左括号的个数。
那么当high小于0时，说明就算把星号都当作左括号了，还是不够抵消右括号，返回false。而当low大于0时，说明左括号的个数太多了，没有足够多的右括号来抵消，返回false。
那么开始遍历字符串，当遇到左括号时，low和high都自增1；当遇到右括号时，只有当low大于0时，low才自减1，保证了low不会小于0，而high直接自减1；当遇到星号时，只有当low大于0时，low才自减1，
保证了low不会小于0，而high直接自增1，因为high把星号当作左括号。当此时high小于0，说明右括号太多，返回false。当循环退出后，我们看low是否为0.
"""


class Solution(object):
    def isValid(self, s):
        low, high = 0, 0
        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                if low > 0:
                    low -= 1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            if high < 0:
                return False
        return low == 0











"""
思路：这道题让我们验证括号字符串，跟之前那道Valid Parentheses有些类似。不同之处在于这道题只有小括号，不过还存在星号，星号可以当左括号，右括号，或空来使用，问我们能不能得到一个合法的括号字符串。
那么我们想，如果不存在星号，那么这题是不是异常的简单，我们甚至连stack都可以不用，直接用一个变量，遇到左括号，自增1，遇到右括号，如果变量为0，直接返回false，否则自减1，最后只要看变量是否为0即可。
但是由于星号的存在，这道题难度就变的复杂了，由于星号可以当括号用，所以当遇到右括号时，就算此时变量为0，也可以用星号来当左括号使用。那么星号什么时候都能当括号来用吗，我们来看两个例子 *) 和 *( ，
在第一种情况下，星号可以当左括号来用，而在第二种情况下，无论星号当左括号，右括号，还是空，*( 都是不对的。当然这种情况只限于星号和左括号之间的位置关系，而只要星号在右括号前面，就一定可以消掉右括号。
那么我们使用两个stack，分别存放左括号和星号的位置，遍历字符串，当遇到星号时，压入星号栈star，当遇到左括号时，压入左括号栈left，当遇到右括号时，此时如果left和star均为空时，直接返回false；
如果left不为空，则pop一个左括号来抵消当前的右括号；否则从star中取出一个星号当作左括号来抵消右括号。当循环结束后，我们希望left中没有多余的左括号，就算有，我们可以尝试着用星号来抵消，当star和left均不为空时，
进行循环，如果left的栈顶左括号的位置在star的栈顶星号的右边，那么就组成了 *( 模式，直接返回false；否则就说明星号可以抵消左括号，各自pop一个元素。最终退出循环后我们看left中是否还有多余的左括号，没有就返回true，否则false

"""


# Time Limit Exceed - 超时！！C++没问题
class Solution(object):
    def isValid(self, s):
        left = []
        star = []
        dict = {")": ["(", "*"]}
        for i in s:
            if i == "(":
                left.append(i)
            elif i == "*":
                star.append(i)
            elif i in dict:
                if left == [] and star == []:
                    return False
                elif left != []:
                    left.pop()
                else:
                    star.pop()

        while left != [] and star != []:
            if len(left) > len(star):
                return False
        return left == []
