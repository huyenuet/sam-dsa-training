from copy import deepcopy
from data_structures.linked_lists.linked_list import LinkedList


# Time complexity O(N)
def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """

    new_list = LinkedList()

    node = deepcopy(linked_list.head)

    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to 
    # the new linked list
    while node:
        old_head = new_list.head
        new_node = node
        node = node.next

        new_node.next = old_head
        new_list.head = new_node
    return new_list


list1 = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    list1.append(value)

print("Pass" if (list(list1) == list(reverse(reverse(list1)))) else "Fail")
