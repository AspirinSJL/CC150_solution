from single_linked_list import Node, LinkedList

@classmethod
def from_addition(cls, l0, l1):
    n0 = l0.head.next
    n1 = l1.head.next
    head = Node()
    current = head

    carry = 0
    while n0 or n1 or carry:
        addition = carry
        if n0:
            addition += n0.val
            n0 = n0.next
        if n1:
            addition += n1.val
            n1 = n1.next
        current.next = Node(val=(addition % 10))
        current = current.next
        carry = addition / 10

    return cls(head.next, True)

setattr(LinkedList, 'from_addition', from_addition)

val_list_1 = [3, 7, 5]
linked_list_1 = LinkedList.from_val_list(val_list_1)
val_list_2 = [9, 7, 3, 7, 2]
linked_list_2 = LinkedList.from_val_list(val_list_2)
linked_list_3 = LinkedList.from_addition(linked_list_1, linked_list_2)
print linked_list_1
print linked_list_2
print linked_list_3