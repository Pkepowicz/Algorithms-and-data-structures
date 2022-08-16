from math import pow
from collections import deque
from time import time

TOWER_SIZE = 4

###########################################################
#           PODEJSCIE REKURENCYJNE
def hanoi_Rec(n, sour, s, dest, d, buff, b, moves) -> None:
    if n == 1:
        dest.insert(0,sour.pop(0))
        moves.append('Z ' + s + " przeniesiono na " + d)
    else:
        hanoi_Rec(n - 1, sour, s, buff, b, dest, d, moves)
        dest.insert(0, sour.pop(0))
        moves.append('Z ' + s + " przeniesiono na " + d)
        hanoi_Rec(n - 1, buff, b, dest, d, sour, s, moves)

file = open('odpowiedzi_rek.txt', 'w')
source = [i for i in range(1, TOWER_SIZE + 1)]
destination, buffer = [], []
moves = []
s, d, b = '1', '2', '3'

hanoi_Rec(TOWER_SIZE, source, s, destination, d, buffer, b, moves)
for i in moves:
    file.write(i + '\n')
file.write('Wystarczylo: ' + str(len(moves)) + ' ruchow')
file.close()

############################################################
#           PODEJSCIE ITERACYJNE
def hanoi_Iter(n, sour:list, dest:list, buff:list, moves) -> None:
    if n % 2 == 0: #zamiana wiezy docelowej
        buff, dest = dest, buff
        dt, bf = '3', '2'
    else:
        dt, bf = '2', '3'
    for i in range(1, int(pow(2, n))):
        if i%3 == 1:
            if len(dest) == 0:
                dest.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + dt)
            elif len(sour) == 0:
                sour.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na 1")
            elif sour[0] < dest[0]:
                dest.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + dt)
            elif dest[0] < sour[0]:
                sour.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na 1")
        if i%3 == 2:
            if len(buff) == 0:
                buff.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + bf)
            elif len(sour) == 0:
                sour.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na 1")
            elif buff[0] < sour[0]:
                sour.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na 1")
            elif sour[0] < buff[0]:
                buff.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + bf)
        if i%3 == 0:
            if len(dest) == 0:
                dest.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na " + dt)
            elif len(buff) == 0:
                buff.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na " + bf)
            elif buff[0] < dest[0]:
                dest.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na " + dt)
            elif dest[0] < buff[0]:
                buff.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na " + bf)
        i += 1

file = open('odpowiedzi_iter.txt', 'w')
source = [i for i in range(1, TOWER_SIZE + 1)]
destination, buffer, moves = [], [], []

hanoi_Iter(TOWER_SIZE, source, destination, buffer, moves)
for i in moves:
    file.write(i + '\n')
file.write('Wystarczylo: ' + str(len(moves)) + ' ruchow')
file.close()

###########################################################
#           CZAS WYKONYWANIA
ITERATIONS = [3, 4, 6, 9, 10, 12, 15, 16, 20]
times_iter, times_rec = [], []
file = open("czasy.txt", 'w')

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

file.write("Czasy wykonywania algorytmow: \n wysokosc wiezy \t czas iteracyjny \t czas rekurencyjny \n")
for i in range(len(ITERATIONS)):
    file.write(str(ITERATIONS[i]) + '\t' + str(times_iter[i]) + '\t' + str(times_rec[i]) + '\n')