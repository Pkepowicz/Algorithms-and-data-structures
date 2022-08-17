import random
import time
from math import floor
from texttable import Texttable


def insertionsort(A):
    for i in range(len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x
    return A


def mergesort(A, a, b):
    if a < b:
        c = floor((a + b) / 2)
        mergesort(A, a, c)
        mergesort(A, c + 1, b)
        merge(A, a, c, b)


def merge(A, a, c, b):
    list = []
    i = a
    j = c + 1
    while i <= c and j <= b:
        if A[i] <= A[j]:
            list.append(A[i])
            i += 1
        else:
            list.append(A[j])
            j += 1
    while i <= c:
        list.append(A[i])
        i += 1
    while j <= b:
        list.append(A[j])
        j += 1
    for l in range(a, b + 1):
        A[l] = list[l - a]


def sum(T):
    a = 0
    for i in T:
        a += i
    return a

# Checking times of both sorts

time_merge, time_insert = [], []
for k in range(100):
    tab = [random.randint(1, 1000) for i in range(5000)]
    list1 = tab
    list2 = tab

    start_insert = time.time()
    insertionsort(list1)
    time_insert.append(time.time() - start_insert)

    start_merge = time.time()
    mergesort(list2, 0, len(list2) - 1)
    time_merge.append(time.time() - start_merge)

time_insert.sort()
time_merge.sort()

table = Texttable()
table.add_rows([["5000 sample", "Insertion sort", "Merge sort"],
                ["sum", sum(time_insert), sum(time_merge)],
                ["Avg", sum(time_insert) / len(time_insert), sum(time_merge) / len(time_merge)],
                ["Min", time_insert[0], time_merge[0]],
                ["Max", time_insert[-1], time_merge[-1]]])

f = open('times.txt', 'w')
f.write(table.draw())
f.close()
