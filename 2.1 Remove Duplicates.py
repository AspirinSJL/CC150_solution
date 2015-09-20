from sets import Set
from single_linked_list import Node, LinkedList

def remove_duplicates(self):
    if self.head.next == None or self.head.next.next == None:
        return 

    before = self.head
    current = before.next
    unique = Set([])
    while current:
        if current.val in unique:
            before.next = current.next
        else:
            unique.add(current.val)
            before = current
        current = current.next

setattr(LinkedList, 'remove_duplicates', remove_duplicates)

val_list = [1, 2, 3, 2, 1, 1, 4]
linked_list = LinkedList.from_val_list(val_list)
print linked_list
linked_list.remove_duplicates()
print linked_list

def is_head_unique(self):
    if self == None or self.next == None:
        return True

    current = self
    val = current.val
    current = current.next
    while current:
        if current.val == val:
            return False
        current = current.next
    return True

setattr(Node, 'is_head_unique', is_head_unique)

def remove_duplicates_no_buffer(self):
    if self.head.next == None or self.head.next.next == None:
        return

    before = self.head
    current = before.next
    while current:
        if current.is_head_unique() == False:
            before.next = current.next
        else:
            before = current
        current = current.next

setattr(LinkedList, 'remove_duplicates_no_buffer', remove_duplicates_no_buffer)

val_list = [1, 2, 3, 2, 1, 1, 4]
linked_list = LinkedList.from_val_list(val_list)
print linked_list
linked_list.remove_duplicates_no_buffer()
print linked_list

