import os
import random

def gen_element():

    key = random.randint(0, 10**7)
    return key

def gen_push():
    return (1, gen_element())
def gen_pop():
    return(2)
def gen_getTop():
    return (3)


def operation_sequences(filename, total_operations):
    with open(filename, 'w') as f:
        f.write(str(f"{total_operations}\n"))

        for i in range(total_operations):
            operation_to_perform = random.randint(1,3)

            if operation_to_perform == 1:
                operation_1 = gen_push()
                f.write(f"{operation_1[0]}\n")
                f.write(f"{operation_1[1]}\n")

            elif operation_to_perform == 2:
                operation_2 = gen_pop()
                f.write(f"{operation_2}\n")

            elif operation_to_perform == 3:
                operation_3 = gen_getTop()
                f.write(f"{operation_3}\n")

class competitior_array:

    def __init__(self):
        self.length = 10**6
        self.A = [0] * self.length
        self.cnt = 0 #current number of elements in A
        self.imax = -1
    
    def push(self,key):
        self.A[self.cnt] = key
        if self.imax == -1 or self.A[self.imax] < self.A[self.cnt]:
            self.imax = self.cnt
        self.cnt = self.cnt + 1
        
    def pop(self):
        if self.imax == -1:
            return None
        keymax = self.A[self.imax]
        self.A[self.imax],self.A[self.cnt-1] = self.A[self.cnt-1],self.A[self.imax]
        self.cnt = self.cnt -1
        if self.cnt == 0:
            self.imax = -1
        else:
            i = 0
            for j in range(0,self.cnt):
                if self.A[j] > self.A[i]:
                    i = j
            self.imax = i
        return keymax
    
    def getTop(self):
        if self.imax == -1:
            return None
        keymax = self.A[self.imax]
        return keymax
        
class max_heap:
    def __init__(self):
        self.length = 10**6
        self.maxheap = [0] * self.length
        self.size = 0

    def push(self,key):
        self.maxheap[self.size] = key
        self.size = self.size + 1
        self.bubble_up(self.size-1)

    def pop(self):
        if self.size == 0:
            return None
        keymax = self.maxheap[0]
        self.maxheap[0], self.maxheap[self.size-1] = self.maxheap[self.size-1], self.maxheap[0]
        self.size = self.size - 1
        self.bubble_down(0)
        return keymax

    def getTop(self):
        if self.size == 0:
            return None
        return self.maxheap[0]
    
    def bubble_up(self, i):
        while True:

            if i == 0:
                break
            if self.maxheap[i] <= self.maxheap[(i-1)//2]:
                break

            self.maxheap[i], self.maxheap[(i-1)//2] = self.maxheap[(i-1)//2], self.maxheap[i]
            i = (i-1)//2

    def bubble_down(self, i):
        j = None

        while True:
            if i == self.size-1:
                break

            l = 2*i + 1
            if l < self.size:
                j = l
            
            r = 2*i + 2
            if r < self.size and self.maxheap[r] > self.maxheap[l]:
                j = r

            if j is None or self.maxheap[i] >= self.maxheap[j]:
                break

            self.maxheap[i], self.maxheap[j] = self.maxheap[j], self.maxheap[i]
            i = j
            j = None
            
    def heapify(self, array_of_keys):
        self.size = len(array_of_keys)

        for i in range(self.size):
            self.maxheap[i] = array_of_keys[i]

        starting_index = (self.size // 2) -1
        
        for i in range(starting_index, -1, -1):
            self.bubble_down(i)