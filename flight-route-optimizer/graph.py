import csv
import heapq


class Graph:
    def __init__(self):
        self.routes = {}

    def add_edge(self, origin, destination, distance):
        if origin not in self.routes:
            self.routes[origin] = {}
        self.routes[origin] [destination] = int(distance)

    def load_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                origin, destination, distance = row
                self.add_edge(origin, destination, distance)


    def shortest_path(self, start, end):
        queue = [(0, start, [])]
        seen = set()

        while queue:
            (cost, node, path) = heapq.heappop(queue)
            if node in seen:
                continue
            seen.add(node)
            path = path + [node]
            if node == end:
                return (cost, path)
            for neighbor, weight in self.routes.get(node, {}).items():
                heapq.heappush(queue, (cost + weight, neighbor, path))
        return (float("inf"), [])
