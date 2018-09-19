# 用两个队列实现一个栈
from queue import Queue

class Stack:
    def __init__(self):
        self.data = Queue()
        self.help = Queue()

    def push(self, val):
        self.data.put(val)

    def pop(self):
        if not self.data:
            return None
        self.transfer()
        res = self.data.get()
        t = self.data
        self.data = self.help
        self.help = t
        return res

    def transfer(self):
        while self.data.qsize() > 1:
            self.help.put(self.data.get())
        return



