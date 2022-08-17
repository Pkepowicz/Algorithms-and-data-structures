from time import time
from random import shuffle


def opening(path):
    with open(path, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()[2:]]


def exec_time(number):
    temp = opening("packages/packages" + str(number) + ".txt")
    items = [Item(temp[k][0], int(temp[k][1]), int(temp[k][2]), int(temp[k][3])) for k in range(len(temp))]
    backpack = Backpack(number, number)
    start = time()
    backpack.greedy_fill(items)
    stop = time()
    file = open(str(number) + "backpack.txt", "w")
    file.write("Value of items in " + str(number) + " element bacpack: " + str(backpack.value) + '\n'
                + "Execution time " + str(stop - start))
    if number <= 200:
        file.write("\nBackpack state:\n" + backpack.state())


class Item:
    def __init__(self, id, width, height, value):
        self.id = id
        self.value = value
        self.width = width if width >= height else height  # width should be bigger than height
        self.height = height if width >= height else width
        self.size = self.width * self.height
        self.ratio = self.value / self.size

    def get_item(self):
        return "<Item#{id}={value}: {x}x{y}>".format(id=self.id, x=self.width, y=self.height, value=self.value)


class Backpack:
    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.data = [[0] * self.width for k in range(self.height)]
        self.free_space = self.width * self.height
        self.value = 0
        self.available = [list(range(self.height)) for k in range(self.width)]

    def state(self):  # Returns current backpack state, line for returning value is turned off
        temp = ""
        for k in self.data:
            temp += "\n" + ("{:>4} " * self.width).format(*k)
        # temp += "\nValue: %d" % self.value
        return temp

    def try_insert(self, item):
        if self.free_space < item.size:
            return False
        for y in range(len(self.available)):
            for x in self.available[y]:
                if self.check_insertion(x, y, item.height, item.width):
                    self.insert(item, x, y, True)
                    return True
                elif self.check_insertion(x, y, item.width, item.height):
                    self.insert(item, x, y)
                    return True
        return False

    def check_insertion(self, x, y, width, height):
        if y + height <= self.height and x + width <= self.width:
            for i in range(y, y + height):
                for k in range(x, x + width):
                    if self.data[i][k] != 0:
                        return False
            return True
        else:
            return False

    def insert(self, item, x, y, rotate=False):
        width = item.width if not rotate else item.height
        height = item.height if not rotate else item.width
        self.free_space -= item.size
        self.value += item.value
        for i in range(y, y + height):
            for k in range(x, x + width):
                if self.data[i][k] != 0:
                    raise Exception("Trying to fill already filled space")
                self.data[i][k] = item.id
                self.available[i].remove(k)

    def greedy_fill(self, items):
        items_sorted = sorted(items, key=lambda x: x.value, reverse=True)
        for k in items_sorted:
            self.try_insert(k)

    def ratio_fill(self, items, inserted=[]):
        if len(inserted) == 0:
            items_sorted = sorted(items, key=lambda x: x.ratio, reverse=True)
            for k in items_sorted:
                if self.try_insert(k):
                    inserted.append(k)
        else:
            temp = []
            shuffle(inserted)
            for k in inserted:
                if self.try_insert(k):
                    temp.append(k)
            inserted = temp
            for k in items:
                if k not in inserted:
                    if self.try_insert(k):
                        inserted.append(k)

    def random_fill(self, items):
        inserted = []
        shuffle(items)
        for l in range(len(items)):
            if self.try_insert(items[l]):
                inserted.append(items[l])
        return [inserted, self.value]


# Execution times

exec_time(20)
exec_time(100)
exec_time(500)
exec_time(1000)
