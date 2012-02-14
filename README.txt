maxheap.py
Author: Christopher Campo
Email : ccampo.progs@gmail.com

A set of functions to implement a max-heap priority queue in Python.  I wrote this to study for a computer science class exam and figured that it may come in handy some day, so I might as well clean it up and publish it online.

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