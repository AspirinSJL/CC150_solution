from single_linked_list import Node, LinkedList

def kth_to_last(self, k):
    fast = self.head
    slow = self.head
    for i in xrange(k):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    return slow

setattr(LinkedList, 'kth_to_last', kth_to_last)

val_list = [1, 2, 3, 4, 5]
linked_list = LinkedList.from_val_list(val_list)
print linked_list
k = 2
print 'the {k}th to last is {node}'.format(k=k, node=linked_list.kth_to_last(k))