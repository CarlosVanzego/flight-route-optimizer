# I start by importing the csv module, which is used to read and write CSV files in Python
import csv
# Then I'm importing heapq, which is a module that provides an implementation of the heap queue algorithm, also known as the priority queue
# This module is used in Dijkstra's algorithm to efficiently find the shortest path in a graph
import heapq  

# I created the Graph class to represent flight routes between airports
class Graph:
    # Here, I am initializing the graph with an empty dictionary called routes
    # The routes dictionary will hold the edges of the graph, where each key is a node (airport) and the value is another dictionary of the neighbors (connected airports) and their respective distances
    def __init__(self):
        # self.routes is an empty dictionary that will hold the edges of the graph; Edges are the connections between the airports
        self.routes = {}  

    # I created the add_edge method to add edges (flight routes) to the graph; self is the instance of the Graph class, origin is the starting airport, destination is the ending airport, and distance is the distance between the two airports
    def add_edge(self, origin, destination, distance):
        # this if statement checks if the origin airport is already in the routes dictionary
        if origin not in self.routes:
            # If not, in the routes dictionary, I initialize an empty dictionary for that origin; This ensures that each origin airport has its own dictionary of destination airports
            self.routes[origin] = {}
        # This line adds the destination airport and its distance to the origin's dictionary
        # The distance is converted to an integer
        # This ensures that the distance is stored as an integer value 
        self.routes[origin][destination] = int(distance)
    # I created the load_from_csv method to load flight routes from the CSV file I created (routes.cvs)
    # This method takes a filename as an argument and reads the CSV file to populate the graph with edges
    def load_from_csv(self, filename):
        # I'm using a try-except block to handle potential errors when opening the CSV file
        try:
            # This line uses the open() function to open the CSV file in read mode; I'm passing filename which is the name of the CSV file, and newline='' to handle newlines in the file correctly, as csvfile is the file object; this statement ensures that the file is opened in the correct mode and that it will be closed automatically when the block is exited
            with open(filename, newline='') as csvfile:
                # I set the variable reader equal to csv.reader(csvfile) which creates a CSV reader object that will iterate over the lines of the CSV file
                reader = csv.reader(csvfile)
                # This for loop iterates through each row in the CSV file
                # Each row is expected to contain three values: origin, destination, and distance
                for row in reader:
                    # This if statement is for If the length of the row is not equal to 3..
                    if len(row) != 3:
                        # If not, I print a warning message indicating that the row is invalid and skip it so as not to cause an error
                        # This is useful for debugging and ensuring that the CSV file has the correct format
                        # This message will inform the user that the row is invalid and will not be processed
                        print(f"⚠️ Skipping invalid row: {row}")
                        # If the row does not have exactly three elements, it is skipped
                        continue
                    # this line unpacks the row into three variables: origin(airport code), destination (airport code), and distance (distance between the two airports)
                    origin, destination, distance = row
                    # This try-except block is used to handle potential errors when converting the distance to an integer
                    try:
                        # Here I am converting the distance value to an integer to ensure that it is stored as an integer
                        distance = int(distance)
                    # If the conversion fails.. 
                    except ValueError:
                        # I am printing a warning message indicating that the distance value is invalid
                        print(f"⚠️ Invalid distane value in row: {row}")
                        # then I skip the row to avoid processing it
                        continue
                    
                    # I created the origin variable and set it equal to the origin airport code; origin.strip() removes any leading or trailing whitespace from the airport code to ensure that it is clean (meaning no extra spaces)and I use the upper() method to convert it to uppercase
                    origin = origin.strip().upper()
                    # I created the destination variable and set it equal to the destination airport code; destination.strip() removes any leading or trailing whitespace from the airport code to ensure that it is clean (meaning no extra spaces)and I use the upper() method to convert it to uppercase
                    # This ensures that the airport codes are stored in a consistent format
                    destination = destination.strip().upper()

                    # This line adds the edge to the graph by calling the add_edge method
                    # It adds the edge from origin to destination with the specified distance
                    self.add_edge(origin, destination, distance)
                    # This line adds the reverse edge from destination to origin with the same distance because the routes are bidirectional meaning that flights can go in both directions
                    # This is done to ensure that the graph is undirected meaning that the routes can be traveled in both directions
                    self.add_edge(destination, origin, distance)
        # this except block handles the case where the CSV file is not found
        except FileNotFoundError:
            # if not found, I'm printing an error message indicating that the file was not found
            print(f"❌ Error: File '{filename}' not found.")
            # then I exit the program with a non-zero status code to indicate an error
            exit(1)

    # I created the shortest_path method to find the shortest path between two airports using Dijkstra's algorithm
    # This method takes two parameters: origin and destination, which are the starting and ending airports
    # The method returns the cost (distance) and the path taken
    def shortest_path(self, origin, destination):
        # I created a dictionary called distance to store the shortest distance from the origin to each airport; airport is the key and the value is the distance, float ("inf") is used to initialize the distances to infinity and for airport in self.routes is a loop that iterates through the airports in the routes dictionary
        distances = {airport: float("inf") for airport in self.routes}
        # I created previous_nodes which is a dictionary to store the previous node for each airport; this means that it will keep track of the previous airport in the shortest path
        # This is used to reconstruct the path later
        previous_nodes = {airport: None for airport in self.routes}
        # this line sets the distance from the origin airport to itself to 0, this means that the distance from the origin to itself is 0 
        distances[origin] = 0

        # I created a priority queue called queue to store the airports to be processed; this is used to efficiently find the airport with the shortest distance
        # The queue is initialized with the origin airport and its distance (0)
        queue = [(0, origin)]
        # This while loop is used to process the airports in the priority queue
        # It continues until the queue is empty
        while queue:
            # The heapq.heappop function is used to pop the airport with the shortest distance from the queue and I assign it to the variables current_distance and current_node
            current_distance, current_node = heapq.heappop(queue)
            # This if statement checks if the current airport has already been processed
            if current_node == destination:
                # if it has been processed, I break out of the loop because this means the shortest path has been found
                break
            # This for loop iterates through the neighbors of the current airport in order to find the shortest path
            # self.routes.get(current_node, {}) returns the dictionary of neighbors for the current airport and .items() returns the key-value pairs (neighbor airport and distance)
            # This means that for each neighbor airport and its distance, I am iterating through the neighbors of the current airport
            for neighbor, weight in self.routes.get(current_node, {}).items():
                # I set the variable new_distance equal to the current distance plus the weight of the edge (distance to the neighbor)
                new_distance = current_distance + weight
                # this if statement checks if the new distance is less than the current distance for the neighbor airport
                if new_distance < distances[neighbor]: 
                    # If it is, I set the distance for the neighbor airport to the new distance
                    distances[neighbor] = new_distance
                    # I also update the previous node for the neighbor airport to the current airport(current_node)
                    previous_nodes[neighbor] = current_node
                    # heapq is a module that provides an implementation of the heap queue algorithm, also known as the priority queue; heappush is used to push the new distance and neighbor airport onto the priority queue; new_distance is the distance to the neighbor airport and neighbor is the airport code
                    heapq.heappush(queue, (new_distance, neighbor))

        # I created the path variable and set it equal to an empty list; this will be used to store the airports in the shortest path
        path = []
        # current is set to the destination airport because this is where the path will end
        # This means that the path will be reconstructed from the destination airport back to the origin airport
        current = destination
        # This while loop is used to reconstruct the path from the destination airport back to the origin airport; If the previous node for the current airport is not None, it means that there is a valid path
        while current is not None:
            # path.insert is used to insert the current airport at the beginning of the path, and I'm passing 0 as the index to insert at the beginning, and current is the airport code
            path.insert(0, current)
            # Here, current is updated to the previous node for the current airport
            # This means that the path will be reconstructed by following the previous nodes from the destination airport back to the origin airport
            current = previous_nodes[current]
        # This if statement checks if the distance to the destination airport is still infinity 
        if distances[destination] == float("inf"):
            # If it is, it means that there is no valid path from the origin to the destination airport; float("inf") is used to represent infinity, [] is an empty list
            return float("inf"), []
        # Finally I return the distance to the destination airport and the reconstructed path
        return distances[destination], path   


    