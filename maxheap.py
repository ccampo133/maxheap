# Christopher Campo
# origin: 12 Feb, 2012
# maxheap.py
'''
maxheap.py
Author: Christopher Campo
Email : ccampo.progs@gmail.com

A set of functions to implement a max-heap priority queue in Python.  I wrote
this to study for a computer science class exam and figured that it may come 
in handy some day, so I might as well clean it up and publish it online.

Functions:
----------
heapify     - convert a list/array into a binary max-heap.
push_heap   - pushes a value onto the heap, maintaining the heap property. 
pop_heap    - pops the max value from the heap, maintaining the heap property.
replace_key - replace a value on the heap with a different one.

See the docstrings of the individual functions for more information on them.

Usage:
------
>>> import maxheap
>>> x = [1, 2, 3, 4, 5]            # initial array
>>> maxheap.heapify(x)             # create max heap
>>> print(x)
[5, 4, 3, 1, 2]
>>> maxheap.push_heap(x, 100)      # push 100 onto the heap
>>> print(x)
[100, 4, 5, 1, 2, 3]
>>> maxval = maxheap.pop_heap(x)   # pop 100 back off
>>> print(x, maxval)
([5, 4, 3, 1, 2], 100)
>>> maxheap.replace_key(x, 4, 215) # replace node 4 (val 2) with val 215
>>> print(x)
[215, 5, 3, 1, 4]
'''

# runs in linear time
def heapify(A):
    '''Turns a list `A` into a max-ordered binary heap.'''
    n = len(A) - 1
    # start at last parent and go left one node at a time
    for node in range(n/2, -1, -1):
        __siftdown(A, node)
    return

# runs in log(n) time
def push_heap(A, val):
    '''Pushes a value onto the heap `A` while keeping the heap property 
    intact.  The heap size increases by 1.'''
    A.append(val)
    __siftup(A, len(A) - 1)   # furthest left node
    return

# runs in log(n) time
def pop_heap(A):
    '''Returns the max value from the heap `A` while keeping the heap
    property intact.  The heap size decreases by 1.'''
    n = len(A) - 1
    __swap(A, 0, n)
    max = A.pop(n)
    __siftdown(A, 0)
    return max

# runs in log(n) time
def replace_key(A, node, newval):
    '''Replace the key at node `node` in the max-heap `A` by `newval`.
    The heap size does not change.'''
    curval  = A[node]
    A[node] = newval
    # increase key
    if newval > curval:
        __siftup(A, node)
    # decrease key
    elif newval < curval:
        __siftdown(A, node)
    return
    
def __swap(A, i, j):
    # the pythonic swap
    A[i], A[j] = A[j], A[i]
    return

# runs in log(n) time   
def __siftdown(A, node):
    '''Traverse down a binary tree `A` starting at node `node` and 
    turn it into a max-heap'''
    child = 2*node + 1
    # base case, stop recursing when we hit the end of the heap
    if child > len(A) - 1:
        return
    # check that second child exists; if so find max
    if (child + 1 <= len(A) - 1) and (A[child+1] > A[child]):
        child += 1
    # preserves heap structure
    if A[node] < A[child]:
        __swap(A, node, child)
        __siftdown(A, child)
    else:
        return

# runs in log(n) time    
def __siftup(A, node):
    '''Traverse up an otherwise max-heap `A` starting at node `node`
    (which is the only node that breaks the heap property) and restore 
    the heap structure.'''
    parent = (node - 1)/2
    if A[parent] < A[node]:
        __swap(A, node, parent)
    # base case; we've reached the top of the heap
    if parent <= 0:
        return
    else:
        __siftup(A, parent)