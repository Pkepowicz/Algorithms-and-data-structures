from time import time
from texttable import Texttable

def test(matrix):
    times = [len(matrix.get_matrix()[0])]
    start = time()
    result = matrix.naive_search()
    stop = time()
    times.append(stop - start)
    times.append(float(len(result)))
    start = time()
    result = matrix.rabin_karp()
    stop = time()
    times.append(stop - start)
    times.append(float(len(result)))
    return times

class Table:

    def __init__(self, path):
        file = open(path)
        self.matrix = [k.strip() for k in file]
        file.close()

    def get_matrix(self):
        return self.matrix

    def print_table(self):
        print(self.matrix)

    def naive_search(self, pattern='ABC'):
        result = []
        for x in range(len(self.matrix) - len(pattern)):
            for y in range(len(self.matrix[x])):
                if self.matrix[x][y] == pattern[0]:
                    if self.matrix[x][y:y + len(pattern)] == pattern:
                        if pattern == "".join(self.matrix[k][y] for k in range(x, x + len(pattern))):
                            result.append((x, y))
        return result

    def rabin_karp(self, pattern = 'ABC', d = 16, q = 13):
        matrixlen = len(self.matrix)
        patternlen = len(pattern)
        h = (d ** (patternlen - 1)) % q
        result = set()
        for x in range(matrixlen - 2):
            p = 0
            t = 0
            for i in range(patternlen):
                p = (d * p + ord(pattern[i])) % q
                t = (d * t + ord(self.matrix[x][i])) % q
            for y in range(matrixlen - patternlen + 1):
                if p == t:
                    if self.matrix[x][y:y + patternlen] == pattern:
                        if pattern == "".join(self.matrix[k][y] for k in range(x, x + patternlen)):
                            result.add((x, y))
                if y < matrixlen - patternlen:
                    t = ((t - h * ord(self.matrix[x][y])) * d + ord(self.matrix[x][y + patternlen])) % q
        return result


p1, p2, p3, p4, p5, p8 = "patterns/1000_pattern.txt", "patterns/2000_pattern.txt", \
                         "patterns/3000_pattern.txt", "patterns/4000_pattern.txt", \
                         "patterns/5000_pattern.txt", "patterns/8000_pattern.txt"
matrix1, matrix2, matrix3, matrix4, matrix5, matrix8 = Table(p1), Table(p2), Table(p3), Table(p4), Table(p5), Table(p8)
times = []

times.append(test(matrix1))
times.append(test(matrix2))
times.append(test(matrix3))
times.append(test(matrix4))
times.append(test(matrix5))
times.append(test(matrix8))

table = Texttable()
table.add_rows([["size", "naive_time", "naive_result", "rabin_karp_time", "rabin_karp_result"],
                [times[0][0], times[0][1], times[0][2], times[0][3], times[0][4]],
                [times[1][0], times[1][1], times[1][2], times[1][3], times[1][4]],
                [times[2][0], times[2][1], times[2][2], times[2][3], times[2][4]],
                [times[3][0], times[3][1], times[3][2], times[3][3], times[3][4]],
                [times[4][0], times[4][1], times[4][2], times[4][3], times[4][4]],
                [times[5][0], times[5][1], times[5][2], times[5][3], times[5][4]]])

f = open('results.txt', 'w')
f.write(table.draw())
f.close()