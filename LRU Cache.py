"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

"""
思路：解这道题，我们要考虑LRU的特性。要知道哪些缓存元素是最近被访问过的，哪些已经很久没有访问过了。链表是可以做这件事情的，但是链表删除和替换位置的操作复杂性为O(n)O(n)，
为了优化效率，采用双向链表来存储，但是双向链表的查找复杂度仍为O(n)O(n)，这时采用哈希表来达到O(1)O(1)的访问复杂度。

每次访问到一个元素，都将该元素移动到链表的头部。当超过缓存限制时，删除链表尾部的元素，同时从哈希表中删除相应的键值。

"""

class Node(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None     #node本身有pre和next, 针对本题，多加一个参数key
        self.pre = None

class DoubleLinkedList:
    def __init__(self):
        self.header = None               #注意：doublelikedlist的header和tail都是node
        self.tail = None

    def add_first(self, node):           #在双向链表中表头加入node
        if self.header is None:
            self.header = node
            self.tail = node
        else:
            h = self.header
            self.header = node
            node.next = h
            h.pre = node

    def remove(self, node):              #在双向链表中移除node
        pre, next = node.pre, node.next
        if pre:
            pre.next = next
        else:
            self.header = next
        if next:
            next.pre = pre
        else:
            self.tail = pre
        node.pre = None
        node.next = None

    def remove_last(self):                 #在双向链表中移除最后一位，并返回这个node
        if self.tail == None:
            return None
        tail = self.tail
        self.remove(tail)
        return tail


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.linkedlist = DoubleLinkedList()
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        self.linkedlist.remove(node)
        self.linkedlist.add_first(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.map:
            self.count += 1
            node = Node(key, value)
            self.map[key] = node
            self.linkedlist.add_first(node)
        else:
            node = self.map[key]
            node.val = value
            self.linkedlist.remove(node)
            self.linkedlist.add_first(node)
        if self.count > self.capacity:
            self.count -= 1
            tail = self.linkedlist.remove_last()
            del self.map[tail.key]
