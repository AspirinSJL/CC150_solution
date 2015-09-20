from single_linked_list import Node, LinkedList

# When val is large, user insert
def partition_swap(self, x):
    traverse = self.head.next
    while traverse and traverse.val < x:
        traverse = traverse.next
    if traverse == None or traverse.next == None:
        return

    eg_begin = traverse
    traverse = traverse.next
    while traverse != None:
        if traverse.val < x:
            eg_begin.val, traverse.val = traverse.val, eg_begin.val
            eg_begin = eg_begin.next
        traverse = traverse.next
    return eg_begin

setattr(LinkedList, 'partition_swap', partition_swap)

def partition_weave(self, x):
    traverse = self.head.next
    l_begin = None
    eg_begin = None

    while traverse != None:
        traverse_next = traverse.next
        if traverse.val < x:
            traverse.next = l_begin
            l_begin = traverse
        else:
            traverse.next = eg_begin
            eg_begin = traverse
        traverse = traverse_next

    if l_begin == None:
        self.head.next = eg_begin
        return eg_begin
    else:
        self.head.next = l_begin
        while l_begin.next != None:
            l_begin = l_begin.next
        l_begin.next = eg_begin
        return eg_begin

setattr(LinkedList, 'partition_weave', partition_weave)

val_list = [1, 5, 3, 2, 1, 1, 4]
linked_list = LinkedList.from_val_list(val_list)
print linked_list
linked_list.partition_swap(3)
print linked_list
linked_list.partition_weave(2)
print linked_list