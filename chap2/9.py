# 用两个栈实现队列
class Queue:
    def __init__(self):
        self.data = []
        self.help = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if len(self.help) != 0:
            return self.help.pop()
        elif not self.data:
            return None
        else:
            self.transfer()
            val = self.help.pop()
            return val

    def transfer(self):
        if len(self.data) == 0:
            return
        while len(self.data) != 0:
            self.help.append(self.data.pop())



