class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def convert_linked_list_to_set(llist: LinkedList):
    output_set = set()
    node = llist.head
    while node:
        output_set.add(node.value)
        node = node.next
    return output_set


def convert_set_to_linked_list(input_set: set):
    ll = LinkedList()
    for item in input_set:
        ll.append(item)

    return ll


def union(llist_1, llist_2):
    union_set = convert_linked_list_to_set(llist_1)
    union_set.union(convert_linked_list_to_set(llist_2))
    return convert_set_to_linked_list(union_set)


def intersection(llist_1, llist_2):
    set_1 = convert_linked_list_to_set(llist_1)
    set_2 = convert_linked_list_to_set(llist_2)

    intersection_set = set_1.intersection(set_2)
    return convert_set_to_linked_list(intersection_set)


# Test case 1
print("Test case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Linked list 1: ", linked_list_1)
print("Linked list 2: ", linked_list_2)
print("Union        : ", union(linked_list_1, linked_list_2))
print("Intersection : ", intersection(linked_list_1, linked_list_2))


# Test case 2
print("\nTest case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Linked list 1: ", linked_list_3)
print("Linked list 2: ", linked_list_4)
print("Union        : ", union(linked_list_3, linked_list_4))
print("Intersection : ", intersection(linked_list_3, linked_list_4))


# Test case 3
print("\nTest case 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1, 3, 5]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("Linked list 1: ", linked_list_5)
print("Linked list 2: ", linked_list_6)
print("Union        : ", union(linked_list_5, linked_list_6))
print("Intersection : ", intersection(linked_list_5, linked_list_6))

