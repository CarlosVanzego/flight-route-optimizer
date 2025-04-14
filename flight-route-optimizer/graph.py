import csv

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
