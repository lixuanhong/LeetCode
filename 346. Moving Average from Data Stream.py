"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

"""
思路：这道题定义了一个MovingAverage类，里面可以存固定个数字，然后我们每次读入一个数字，如果加上这个数字后总个数大于限制的个数，那么我们移除最早进入的数字，然后返回更新后的平均数，
这种先进先出的特性最适合使用队列queue来做，而且我们还需要一个double型的变量sum来记录当前所有数字之和，这样有新数字进入后，如果没有超出限制个数，则sum加上这个数字，如果超出了，
那么sum先减去最早的数字，再加上这个数字，然后返回sum除以queue的个数。
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = collections.deque()
        sum = 0.0               #注意：这里求平均值有除法是double, 容易犯错！！


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) >= self.size:
            item = self.queue.popleft()
            sum -= item                #sum需要扣除pop掉的那个元素
        self.queue.append(val)
        sum += val
        return sum / len(self.queue)
