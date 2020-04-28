class MinHeap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def size(self):
        return self.next_index

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = (parent_index * 2) + 1
            right_child_index = (parent_index * 2) + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            min_element = parent

            if left_child is not None:
                min_element = min(parent, left_child)

            if right_child is not None:
                min_element = min(parent, right_child)

            # parent is at the right place
            if min_element == parent:
                return

            # left child is the min element, should be move to parent's position
            if min_element == left_child:
                self.cbt[parent_index] = left_child
                self.cbt[left_child_index] = parent
                parent_index = left_child_index

            # right_child is the min element, should be move to parent's position
            if min_element == right_child:
                self.cbt[parent_index] = right_child
                self.cbt[right_child_index] = parent
                parent_index = right_child_index

    def remove(self):
        # if heap is empty
        if self.size() == 0:
            return None

        # remove the root
        last_element = self.cbt[self.next_index-1]
        to_remove = self.cbt[0]

        # firstly, move last child to the root
        self.cbt[0] = last_element

        # secondly, decrease next_index by 1
        self.next_index -= 1

        # down heapify
        self._down_heapify()

        # store to_remove element to free space of the heap, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove

        return to_remove

    def get_minimum(self):
        return self.cbt[0]

    def is_empty(self):
        return self.size() == 0


heap = MinHeap(1)
heap.insert(10)
print(heap.cbt)

heap.insert(2)
heap.insert(3)
print(heap.cbt)

print("to_remove: ", heap.remove())
print(heap.cbt)

print("to_remove: ", heap.remove())
print(heap.cbt)

print("to_remove: ", heap.remove())
print(heap.cbt)
