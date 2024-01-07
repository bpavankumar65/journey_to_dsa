class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, val):
        self.head = ListNode(val)
        self.tail = self.head

    def insert_node_at_begining(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def insert_at_given_position(self, index, val):
        newNode = ListNode(val)
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1
        if curr.next:
            if curr.next == self.tail:
                newNode.next = self.tail
                curr.next = newNode
            else:
                curr.next = newNode
                newNode.next = curr.next.next

    def delete_first_node(self):
        curr = self.head
        self.head = curr.next
        curr.next = None

    def del_last_node(self):
        curr = self.head
        while curr:
            if curr.next == self.tail:
                curr.next = None
                self.tail = curr
            curr = curr.next

    def search_value_index(self, val):
        curr = self.head
        i = 0
        while curr:
            if curr.val == val:
                return i
            i += 1
            curr = curr.next
        return -1

    def print(self):
        curr = self.head
        while curr:
            print("element {}", curr.val)
            curr = curr.next


linked_list = LinkedList(3)
linked_list.insert_at_end(4)
linked_list.insert_node_at_begining(2)
linked_list.insert_node_at_begining(1)
linked_list.insert_at_given_position(2, 5)
linked_list.delete_first_node()
linked_list.del_last_node()
print(linked_list.search_value_index(3))
linked_list.print()
