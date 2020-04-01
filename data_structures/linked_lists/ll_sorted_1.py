from data_structures.linked_lists.sorted_linked_list import SortedLinkedList


# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print("Pass" if (node.value == 4) else "Fail")

linked_list.append(3)
node = linked_list.head.next.next
print("Pass" if (node.value == 3) else "Fail")
