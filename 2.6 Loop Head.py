from single_linked_list import Node, LinkedList

def loop_head(self):
    fast = self.head
    slow = self.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return None
    
    p0 = self.head
    p1 = fast
    while p0 != p1:
        p0 = p0.next
        p1 = p1.next
    return p0

setattr(LinkedList, 'loop_head', loop_head)

val_list = [1, 2, 3, 4, 5]
linked_list = LinkedList.from_val_list(val_list)
linked_list.last().next = linked_list.head.next.next.next
print linked_list.loop_head().val