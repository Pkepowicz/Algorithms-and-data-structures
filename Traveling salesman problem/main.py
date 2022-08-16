class map:
    def __init__(self, path):
        file = open(path, "r")
        self.map = {}
        for line in file:
            self.map[line.split()[0]] = line.split()[1:]
        file.close()

    def get_X(self, key):
        return float(self.map[key][0])

    def get_Y(self, key):
        return float(self.map[key][1])

    def calculate_distance(self, key1, key2):
        return ((self.get_X(key1) - self.get_X(key2))**2 + (self.get_Y(key1) - self.get_Y(key2))**2)**0.5

    def simple_route(self):
        route = [list(self.map.keys())[0]]
        lenght = 0
        for i in range(1, len(self.map)):
            lenght += self.calculate_distance(str(i), str(i+1))
            route.append(list(self.map.keys())[i])
        route.append(list(self.map.keys())[0])
        lenght += self.calculate_distance(list(self.map.keys())[0], list(self.map.keys())[-1])
        return route, lenght

    def planned_route(self):
        visited = [list(self.map.keys())[0]]
        not_visited = list(self.map.keys())[1:]
        lenght = 0
        while not_visited:
            distance_list = [self.calculate_distance(visited[-1], str(k)) for k in not_visited]
            lenght += min(distance_list)
            visited.append(not_visited[distance_list.index(min(distance_list))])
            del not_visited[distance_list.index(min(distance_list))]
        lenght += self.calculate_distance(str(visited[0]), str(visited[-1]))
        visited.append(list(self.map.keys())[0])
        return visited, lenght

    def print(self):
        for line in self.map:
            print(line, self.map[line])


m = map("TSP.txt")
route, lenght = m.simple_route()
for i in range(len(route)):
    print(route[i], ' => ', end='')
print('\n', lenght)
route, lenght = m.planned_route()
for i in range(len(route)):
    print(route[i], ' => ', end='')
print('\n', lenght)