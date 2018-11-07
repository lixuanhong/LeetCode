"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

"""
例如：

输入1：

/../a/b/c/./..

输出1：

/a/b
模拟整个过程：

1. "/" 根目录

2. ".." 跳转上级目录，上级目录为空，所以依旧处于 "/"

3. "a" 进入子目录a，目前处于 "/a"

4. "b" 进入子目录b，目前处于 "/a/b"

5. "c" 进入子目录c，目前处于 "/a/b/c"

6. "." 当前目录，不操作，仍处于 "/a/b/c"

7. ".." 返回上级目录，最终为 "/a/b"

使用一个栈来解决问题。遇到'..'弹栈，遇到'.'不操作，其他情况下压栈。
"""

class Solution(object):
    def simplifyPath(self, path):
        stack = list()
        dirs = path.split('/')
        for dir in dirs:
            if not dir or dir == '.':
                continue
            if dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/' + '/'.join(stack) #join前的连接符‘/’只会用于第一个字符之后

obj = Solution()
path = "/home//foo/"
print(obj.simplifyPath(path))
