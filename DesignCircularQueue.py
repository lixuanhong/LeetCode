"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.


Example:

MyCircularQueue circularQueue = new MycircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
"""

class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = []
        self.size = k


    def enQueue(self, value):
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.queue) == self.size:
            return True
        else:
            return False






#错误写法，但是体现circular queue的原理
#https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.queue = []
        self.front = -1
        self.rear = -1


    def enQueue(self, value):               #O(1)
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFulll():
            return False
        else:
            if self.isEmpty():
                self.front, self.rear = 0, 0
            elif self.rear == self.size - 1:
                self.rear = 0
            else:
                self.rear += 1
            self.queue[self.rear] = value         #这种写法在python里面是错误的！！在python里面不需要用到self.front和self.rear, 因为python的list是动态的
            return True


    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue.pop(self.front)
            if self.front == self.rear:
                self.front, self.rear = -1, -1
            elif self.front == self.size - 1:
                self.front = 0
            else:
                self.front += 1
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]


    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.front == self.rear == -1:
            return True
        else:
            return False


    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (self.front == 0 and self.rear == self.size - 1) or (self.rear + 1 == self.front):
            return True
        else:
            return False
