from single_linked_list import Node, LinkedList

def is_palindrome(self):
    fast = self.head
    slow = self.head
    stack = []

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        stack.append(slow.val)

    if not fast:
        stack.pop()

    slow = slow.next
    while slow and stack.pop() == slow.val:
        slow = slow.next
    return (True if not slow else False)

setattr(LinkedList, 'is_palindrome', is_palindrome)

val_list_1 = [1, 2, 3, 4, 5]
linked_list_1 = LinkedList.from_val_list(val_list_1)
print linked_list_1.is_palindrome()
val_list_2 = [1, 2, 3, 2, 1]
linked_list_2 = LinkedList.from_val_list(val_list_2)
print linked_list_2.is_palindrome()