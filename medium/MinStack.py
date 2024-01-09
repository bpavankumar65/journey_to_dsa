class MinStack(object):

    def __init__(self):
        self._list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self._list.append(val)

    def pop(self):
        """
        :rtype: None
        """
        return self._list.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self._list)
