class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class LinkedList():
    def __init__(self, head=None, has_dummy=False):
        self.head = head
        self.has_dummy = has_dummy
        if self.has_dummy:
            dummy = Node(next=self.head)
            self.head = dummy

    @classmethod
    def from_val_list(cls, val_list, has_dummy=True):
        head = None
        for v in reversed(val_list):
            node = Node(v, head)
            head = node

        return cls(head, has_dummy)
        
    def remove_dummy(self):
        if self.has_dummy:
            self.head = self.head.next
            self.has_dummy = False

    def add_dummy(self):
        if not self.has_dummy:
            dummy = Node(next=self.head)
            self.head = dummy
            self.has_dummy = True

    def last(self):
        node = self.head.next if self.has_dummy else self.head
        if node == None:
            return node
        while node.next:
            node = node.next
        return node

    def __str__(self):
        val_list = []
        current = self.head.next if self.has_dummy else self.head
        while current:
            val_list.append(current.val)
            current = current.next
        return ' '.join([`val` for val in val_list])
