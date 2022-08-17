from math import pow
from time import time
from texttable import Texttable

TOWER_SIZE = 4


###########################################################
#           RECURSIVE APPROACH
def hanoi_Rec(n, sour, s, dest, d, buff, b, moves) -> None:
    if n == 1:
        dest.insert(0, sour.pop(0))
        moves.append('From ' + s + " moved to " + d)
    else:
        hanoi_Rec(n - 1, sour, s, buff, b, dest, d, moves)
        dest.insert(0, sour.pop(0))
        moves.append('From ' + s + " moved to " + d)
        hanoi_Rec(n - 1, buff, b, dest, d, sour, s, moves)


file = open('rec.txt', 'w')
source = [i for i in range(1, TOWER_SIZE + 1)]
destination, buffer = [], []
moves = []
s, d, b = '1', '2', '3'

hanoi_Rec(TOWER_SIZE, source, s, destination, d, buffer, b, moves)
for i in moves:
    file.write(i + '\n')
file.write('Solved in ' + str(len(moves)) + ' moves')
file.close()


############################################################
#           ITERATIVE APPROACH
def move(A: list, B: list) -> bool:
    if not A:
        A.insert(0, B.pop(0))
        return False
    elif not B:
        B.insert(0, A.pop(0))
        return True
    else:
        if A[0] < B[0]:
            B.insert(0, A.pop(0))
            return True
        else:
            A.insert(0, B.pop(0))
            return False


def hanoi_Iter(n, sour: list, dest: list, buff: list, moves: list) -> None:
    if n % 2 == 0:
        buff, dest = dest, buff
        sc, dt, bf = '1', '3', '2'
    else:
        sc, dt, bf = '1', '2', '3'
    for i in range(1, int(pow(2, n))):
        if i % 3 == 1:
            if move(sour, dest):
                moves.append("From " + sc + " moved to " + dt)
            else:
                moves.append("From " + dt + " moved to " + sc)
        if i % 3 == 2:
            if move(sour, buff):
                moves.append("From " + sc + " moved to " + bf)
            else:
                moves.append("From " + bf + " moved to " + sc)
        if i % 3 == 0:
            if move(buff, dest):
                moves.append("From " + bf + " moved to " + dt)
            else:
                moves.append("From " + dt + " moved to " + bf)
        i += 1


file = open('iter.txt', 'w')
source = [i for i in range(1, TOWER_SIZE + 1)]
destination, buffer, moves = [], [], []

hanoi_Iter(TOWER_SIZE, source, destination, buffer, moves)
for i in moves:
    file.write(i + '\n')
file.write('Solved in ' + str(len(moves)) + ' moves')
file.close()

###########################################################
#           Times
ITERATIONS = [3, 4, 6, 9, 10, 12, 15, 16, 20]
times_iter, times_rec = [], []
table = Texttable()
table.add_row(["Height", "Iterative time", "Recursive time"])

for i in ITERATIONS:
    src = [l for l in range(1, i + 1)]
    dt, bf, mv = [], [], []
    start = time()
    hanoi_Rec(i, src, '1', dt, '2', bf, '3', mv)
    times_rec.append(time() - start)

    src = [l for l in range(1, i + 1)]
    dt, bf, mv = [], [], []
    start = time()
    hanoi_Iter(i, src, dt, bf, mv)
    times_iter.append(time() - start)

for i in range(len(ITERATIONS)):
    table.add_row([ITERATIONS[i], times_iter[i], times_rec[i]])

f = open("times.txt", "w")
f.write(table.draw())