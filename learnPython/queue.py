from collections import deque

queue = deque()
queue.append(1)
queue.extend([2, 3, 4])
print(queue)
queue.popleft()


class queue:

    def __init__(self):
        self._list = []

    def append(self, elem):
        return self._list.append(elem)

    def popleft(self):
        return self._list.pop(0)

    def pop(self):
        return self._list.pop()

    def extend(self, elem):
        return self._list.extend(elem)

    def count(self, elem):
        return self._list.count(elem)

    def index(self, elem):
        return self._list.index(elem)

    def __str__(self):
        return 'Queue: ' + str(self._list)


class Stack:
    def __init__(self):
        self._list = []

    def push(self, elem):
        return self._list.append(elem)

    def pop(self):
        return self._list.pop()

    def extend(self):
        return self._list.extend()

    def count(self, elem):
        return self._list.count(elem)

    def index(self, elem):
        return self._list.index(elem)

    def __str__(self):
        return 'Stack: ' + str(self._list)


s = Stack()
s.push(5)
qu = queue()
qu.append(1)
qu.extend([2,3,4])
print(qu)
qu.popleft()
print(qu)
