from typing import List, Dict
import math
from random import randint


class BaseHeap:
    '''
        Base class for heap.
        public methods: insert(), pop_max()
        helper methods: _parent(), _lchild(), _rchild()

        _heapify(), bubble_up(), and filter_down() left for
        implementation of max or min heap
    '''

    def __init__(self, input_list=False):
        self._cont = [0]
        self._size = 0
        if input_list:
            self.heapify(input_list)

    def insert(self, new_value: int):
        self._cont.append(new_value)
        self._size += 1
        self._bubble_up(self._size)

    def pop_priority(self):
        to_return = self._cont[1]
        self._swap(1, self._size)
        del self._cont[self._size]
        self._size -= 1
        self._filter_down(1)
        return to_return

    def _parent(self, index: int):
        return index // 2

    def _lchild(self, index: int):
        return index * 2

    def _rchild(self, index: int):
        return (index * 2) + 1

    def _swap(self, i: int, j: int):
        self._cont[i], self._cont[j] = self._cont[j], self._cont[i]

    def heapify(self, input_list):
        index = len(input_list) // 2
        self._size = len(input_list)
        self._cont = [0] + input_list
        while index > 0:
            self._filter_down(index)
            index -= 1

    def heapify_r(self, input_list):
        index = len(input_list) // 2
        self._size = len(input_list)
        self._cont = [0] + input_list

        def _helper(index):
            if index <= 0:
                return
            self._filter_down(index)
            _helper(index - 1)

        _helper(index)

    def __bool__(self):
        return self._size > 0

    def __repr__(self):
        return f'{self._cont[1:]}'

    def __str__(self):
        size = 2 ** math.ceil(math.log2(self._size + 1)) - 1
        string = ''
        c = 1
        while c <= self._size:
            btwn = size // c
            front = btwn // 2
            string += front * ' '
            string += (' ' * btwn).join(
                [str(i) for i in self._cont[c: c * 2]]) + '\n'
            c *= 2
        return string


class MaxHeap(BaseHeap):
    '''
        Array-based MaxHeap implementation
        inherits public methods: insert, pop_max from BaseHeap
        inherits helper methods: _parent, _lchild, _rchild, _swap from BaseHeap
        implements private methods: _max_heapify, _bubble_up, filter_down
    '''

    def _bubble_up(self, index: int):
        parent = self._parent(index)
        if self._cont[index] > self._cont[parent] and parent > 0:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _filter_down(self, index: int):
        if self._rchild(index) <= self._size:
            larger = max([self._lchild(index), self._rchild(index)],
                         key=lambda x: self._cont[x])
            if self._cont[index] < self._cont[larger]:
                self._swap(index, larger)
                self._filter_down(larger)
        elif self._lchild(index) == self._size:
            if self._cont[index] < self._cont[self._lchild(index)]:
                self._swap(index, self._lchild(index))


class MinHeap(BaseHeap):

    def _bubble_up(self, index: int) -> None:
        parent = self._parent(index)
        if self._cont[index] < self._cont[parent] and parent > 0:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _filter_down(self, index: int) -> None:
        if self._rchild(index) <= self._size:
            smaller = min([self._lchild(index), self._rchild(index)],
                          key=lambda x: self._cont[x])
            if self._cont[index] > self._cont[smaller]:
                self._swap(index, smaller)
                self._filter_down(smaller)
        elif self._lchild(index) == self._size:
            if self._cont[index] > self._cont[self._lchild(index)]:
                self._swap(index, self._lchild(index))


# //TODO//
# Implement heap in which left and right child priority is invariant
# and set during insertion so that it doesn't need to be checked
# during extraction. Not better, just a tradeoff. Right child would always be
# higher priority for min or max heap. Requires idea of sibling.

test = [randint(0,9) for _ in range(31)]

h = MaxHeap(test)
print(h)
