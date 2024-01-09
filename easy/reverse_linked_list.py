class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = ListNode(val)
        self.tail = self.head

    def push(self, value):
        self.tail.next = ListNode(value)
        self.tail = self.tail.next

    def reverse(self):
        prev = None

        curr = self.head
        while curr:
            nxt_value = curr.next
            curr.next = prev
            prev = curr
            curr =  nxt_value
            print("{} -->".format(prev.val))

            # curr = head
            # prev = None
            # while (curr):
            #     nxt_val = curr.next
            #     curr.next = prev
            #     prev = curr
            #     curr = nxt_val
            # return prev
    def recursive_reverse(self, head):
        if not head:
            return None
        NewHead = head
        if head.next:
            NewHead = self.recursive_reverse(head.next)
            head.next.next = head
        head.next = None
        return NewHead




    def print(self):
        curr = self.head
        while curr:
            print("{} -->".format(curr.val))
            curr = curr.next


x = LinkedList(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
x.print()
x.reverse()
x.print()