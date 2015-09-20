from single_linked_list import Node, LinkedList

def del_node(self, node):
    if node == None:
        raise Exception("Node can't be None")
        return
    if node.next == None:
        # Mark it as dummy when it's the last node 
        node.val = -1
        return
    node.val = node.next.val
    node.next = node.next.next

setattr(LinkedList, 'del_node', del_node)

val_list = [1, 2, 3, 4, 5]
linked_list = LinkedList.from_val_list(val_list)
print linked_list
node = linked_list.head.next.next
linked_list.del_node(node)
print linked_list
node = node = linked_list.head.next.next.next.next
linked_list.del_node(node)
print linked_list

