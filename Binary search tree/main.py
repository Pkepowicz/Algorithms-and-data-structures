from bisect import insort
from math import floor
from random import randint
from time import time
from texttable import Texttable

NUMBER_RANGE = 100000

def possible_root_value(data):
    temp = floor(data)
    i = 0.5
    while temp > i:
        i += 1
    if abs(data - i) < abs(data - (i + 1)):
        return i
    else:
        return i + 1

def random_Number():
    return randint(1, NUMBER_RANGE) / 100

def random_List(data):
    result = []
    while len(result) < data:
        temp = random_Number()
        if temp not in result:
            result.append(temp)
    return result

def test_Time(number_Of_Iterations):
    list = random_List((number_Of_Iterations))
    bst = forest(None)
    times = []
    times.append(len(list))
    time_Start = time()
    for i in list:
        bst.insert(i)
    time_End = time()
    times.append(time_End - time_Start)
    time_Start = time()
    bst.minimum(random_Number())
    time_End = time()
    times.append(time_End - time_Start)
    time_Start = time()
    bst.maximum(random_Number())
    time_End = time()
    times.append(time_End - time_Start)
    time_Start = time()
    bst.search(random_Number())
    time_End = time()
    times.append(time_End - time_Start)
    return times

class tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_Data(self):
        return self.data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def minimum(self):
        if self.left:
            return self.left.minimum()
        else:
            return self.data

    def maximum(self):
        if self.right:
            return self.right.maximum()
        else:
            return self.data

    def search(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif self.data < data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def print(self, level = '', indent = ''):
        temp = indent + level + str(self.data)
        level += '-'
        indent += '\t'
        print(temp)
        if self.left:
            self.left.print(level, indent)
        if self.right:
            self.right.print(level, indent)

class forest:

    def __init__(self, data):
        self.root = []
        self.helper = []

    def insert(self, data):
        root_value = possible_root_value(data)
        if root_value in self.helper:
            index = self.helper.index(root_value)
        else:
            insort(self.helper, root_value)
            index = int(self.helper.index(root_value))
            self.root.insert(index, tree(root_value))
        if self.root[index].get_Data() != data:
            self.root[index].insert(data)

    def minimum(self, data):
        if data in self.helper:
            index = self.helper.index(data)
            return self.root[index].minimum()
        else:
            return None

    def maximum(self, data):
        if data in self.helper:
            index = self.helper.index(data)
            return self.root[index].maximum()
        else:
            return None

    def search(self, data):
        root_value = possible_root_value(data)
        if root_value in self.helper:
            index = self.helper.index(root_value)
            return self.root[index].search(data)
        else:
            return False

    def print(self):
        for i in self.root:
            i.print()

file = open('times.txt', 'w')
table = Texttable()

time1 = test_Time(250)
time2 = test_Time(500)
time3 = test_Time(1000)
time4 = test_Time(2500)
time5 = test_Time(5000)
time6 = test_Time(10000)
time7 = test_Time(50000)

table.add_rows([["lenght", "insert", "minimum", "maximum", "search"],
               [time1[0], time1[1], time1[2], time1[3], time1[4]],
               [time2[0], time2[1], time2[2], time2[3], time2[4]],
               [time3[0], time3[1], time3[2], time3[3], time3[4]],
               [time4[0], time4[1], time4[2], time4[3], time4[4]],
               [time5[0], time5[1], time5[2], time5[3], time5[4]],
               [time6[0], time6[1], time6[2], time6[3], time6[4]],
               [time7[0], time7[1], time7[2], time7[3], time7[4]]])
file.write(table.draw())
file.close()
