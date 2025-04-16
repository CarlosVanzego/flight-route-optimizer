# # I am importing the csv module, which is used to read and write CSV files in Python
# import csv
# # I am then printing heapq, which is a module that provides an implementation of the heap queue algorithm, also know as the priority queue
# import heapq

# # I created the Graph class to represent a directed graph
# # The graph will be used to store the flight routes and their distances
# class Graph:
#     # I am initializing the graph with an empty dictionary called routes
#     # The routes dictionary will hold the edges of the graph, where each key is a node (airport) and the value is another dictionary of the neighbors (connected airports) and their respective distances
#     def __init__(self):
#         self.routes = {}
#     # I created the add_edge method to add edges to the graph
#     # This method takes three parameters: origin, destination, and distance
#     def add_edge(self, origin, destination, distance):
#         if origin not in self.routes:
#             self.routes[origin] = {}
#         self.routes[origin] [destination] = int(distance)
#     # I created the load_from_csv method to load flight routes from a CSV file

#     def load_from_csv(self, filename):
#         # this try-except block is used to handle potential errors when opening the CSV file
#         # If the file is not found, it will print an error message and exit the program
#         # If the file is found, it will read the contents and add edges to the graph
#         try:
#             with open(filename, newline='') as csvfile:
#                 reader = csv.reader(csvfile)
#                 for row in reader:
#                     print(f"DEBUG: Reading row: {row}")  # <--- ADD THIS
#                     if len(row) != 3:
#                         print(f"⚠️ Skipping invalid row: {row}")
#                         continue
#                 origin, destination, distance = row
#                 self.add_edge(origin, destination, distance)
#         except FileNotFoundError:
#             print(f"❌ Error: File '{filename}' not found.") 
#             exit(1)       

#     # I created the shortest_path_method to find the shortest path between two nodes (airports) using Dijkstra's algorithm
#     # This method takes two parameters: start and end, which are the starting and ending airports
#     def shortest_path(self, start, end):
#         queue = [(0, start, [])]
#         seen = set()
#         # This while loop is used to process the nodes in the priority queue
#         # It continues until the queue is empty
#         while queue:
#             (cost, node, path) = heapq.heappop(queue)
#             if node in seen:
#                 continue
#             seen.add(node)
#             path = path + [node]
#             if node == end:
#                 return (cost, path)
#             for neighbor, weight in self.routes.get(node, {}).items():
#                 heapq.heappush(queue, (cost + weight, neighbor, path))
#         return (float("inf"), [])


import csv
import heapq  # Priority queue for Dijkstra's algorithm

# Custom class to represent flight routes between airports
class Graph:
    def __init__(self):
        self.routes = {}  # Dictionary of airports and their destination connections

    def add_edge(self, origin, destination, distance):
        # Add one-way route from origin to destination
        if origin not in self.routes:
            self.routes[origin] = {}
        self.routes[origin][destination] = int(distance)

    def load_from_csv(self, filename):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) != 3:
                        print(f"⚠️ Skipping invalid row: {row}")
                        continue
                    origin, destination, distance = row
                    self.add_edge(origin.strip().upper(), destination.strip().upper(), distance)
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found.")
            exit(1)

    def shortest_path(self, start, end):
        # Dijkstra's algorithm for shortest path
        queue = [(0, start, [])]  # (cost_so_far, current_node, path_so_far)
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

        return (float("inf"), [])  # No path found
