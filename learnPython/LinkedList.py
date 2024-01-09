class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class LinkedList:

    def __init__(self):
        self.head = ListNode(5)
        self.tail = self.head

    def insertNodeEnd(self, val):
        self.tail.next = ListNode(val)  # create the node at tail .next
        self.tail = self.tail.next  # now point the node using tail.next and set it as tail

    def removeNode(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr.next
            curr.next = curr.next.next

    def print(self):
        curr = self.head
        while(curr):
            print("---> ", curr.val)
            curr = curr.next

x = LinkedList()
x.insertNodeEnd(6)
x.insertNodeEnd(7)
x.print()
x.removeNode(0)
x.print()
