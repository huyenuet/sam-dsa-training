from data_structures.linked_lists.linked_list import LinkedList


def is_circular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        # if a node refers to itself, that's a little loop
        if slow.next == slow:
            return True

        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two nodes
        fast = fast.next.next

        if slow == fast:
            return True

    # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
    # the list has an end and isn't circular
    return False


list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

print("Pass" if (is_circular(list_with_loop) is True) else "Fail")
print("Pass" if (is_circular(LinkedList([-4, 7, 2, 5, -1])) is False) else "Fail")
print("Pass" if (is_circular(LinkedList([1])) is False) else "Fail")
