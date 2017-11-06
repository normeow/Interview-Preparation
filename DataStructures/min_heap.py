class MinHeap():
    def __init__(self):
        self.data = []

    def build_heap(self, array):
        self.data = array.copy()
        for i in range(self.heap_size() // 2, -1, -1):
            self.heapifyDown(i)

    def heap_size(self):
        return len(self.data)

    def has_parent(self, i):
        return self.get_parent_index(i) >= 0

    def has_left_child(self, i):
        return self.get_left_child_index(i) < self.heap_size()

    def has_right_child(self, i):
        return self.get_right_child_index(i) < self.heap_size()

    def get_parent_index(self, i):
        return (i - 1) // 2

    def get_left_child_index(self, i):
        return i * 2 + 1

    def get_right_child_index(self, i):
        return i * 2 + 2

    def parent(self, i):
        return self.data[self.get_parent_index(i)]

    def left_child(self, i):
        return self.data[self.get_left_child_index(i)]

    def right_child(self, i):
        return self.data[self.get_right_child_index(i)]

    def swap(self, index_1, index_2):
        self.data[index_1], self.data[index_2] = self.data[index_2], self.data[index_1]

    def heapifyDown(self, i):
        minimum_ind = i
        if self.has_left_child(i) and self.data[minimum_ind] > self.left_child(i):
            minimum_ind = self.get_left_child_index(i)
        if self.has_right_child(i) and self.data[minimum_ind] > self.right_child(i):
            minimum_ind = self.get_right_child_index(i)
        if minimum_ind != i:
            self.swap(i, minimum_ind)
            self.heapifyDown(minimum_ind)

    def heapifyUp(self, i):
        if self.has_parent(i) and self.data[i] < self.parent(i):
            parent_index = self.get_parent_index(i)
            self.swap(i, parent_index)
            self.heapifyUp(parent_index)

    def insert(self, x):
        self.data.append(x)
        self.heapifyUp(self.heap_size() - 1)

    def peek(self):
        if self.heap_size() == 0:
            raise Exception("Heap is empty")
        return self.data[0]

    def extract_min(self):
        if self.heap_size() == 0:
            raise Exception("Heap is empty")
        min_element = self.data[0]
        self.data[0] = self.data.pop()
        self.heapifyDown(0)
        return min_element
