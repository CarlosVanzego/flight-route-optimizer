# I start by importing the argparse module, which allows me to handle command-line arguments in a clean and user-friendly way
import argparse
# Then, from the graph module, I import the Graph class, which is I define in another file called graph.py
# This class will be used to manage the flight routes and perform the shortest path calculations
from graph import Graph

# Here I created the CLI parser using argparse
# I set parser equal to argparse.ArgumentParser, which is a built-in Python class that makes it easy to write user-friendly command-line interfaces
# Description is set equal to a string that describes what the script does
# This description will be displayed when the user runs the script with the --help flag
parser = argparse.ArgumentParser(description="Find shortest flight route between two airports.")
# This first parser.add_argument is for the origin airport code, type=str inidicates that the input should be a string (help provides a short explanation of what this argument is for) and I give an example of a valid input "BWI"; This means the user must supply an airport code like (e.g., BWI) as the first argument
parser.add_argument("origin", type=str, help="Origin airport code (e.g., BWI)")
# This second parser.add_argument is for the destination airport code, type=str indicates that the input should be a string (help provides a short explanation of what this argument is for) and I give an example of a valid input "HOU"; This means the user must supply an airport code like (e.g., HOU) as the second argument
parser.add_argument("destination", type=str, help="Destination airport code (e.g., HOU)")
# This optional argument allows the user to specify a different CSV file for the routes; --debug means this is an optional argument, action="store_true" means that if the argument is provided, it will be set to True, and if not, it will be False; Help provides a short explanation of what this argument does
parser.add_argument("--debug", action="store_true", help="Show route graph data for debugging")

# I created the variable args and store the parsed arguments in it; this is done by calling parser.parse_args(), which processes the command-line arguments and stores them in the args variable
# For example, if the user runs `python main.py BWI HOU`, then:
# args.origin = "BWI" and args.destination = "HOU"
args = parser.parse_args()

# I created an instance of the Graph class
graph = Graph()
# Then I load the routes from a CSV file into the graph instance; data/routes.csv is the default file name and path
graph.load_from_csv("data/routes.csv")

# I created the all_airports variable, which is set to a set of all airport codes in the graph
all_airports = set(graph.routes.keys())
# for in neighbors in graph.routes.values(): is a loop that iterates through the values of the graphs routes dictionary
# In this case, each value is a dictionary of neighboring airports and their distances
for neighbors in graph.routes.values():
    # Here I am updating the all_airports set with the keys of the neighbors dictionary
    # This means I am adding all destination airports to the all_airports set
    # This ensures that all airports in the graph are included in the all_airports set
    all_airports.update(neighbors.keys())

# This if statement validates that the user-input airports actually exist in the data
if args.origin not in all_airports:
    # Then i'm printing an error message if the origin airport code is not found in the all_airports set
    # This message will inform the user that the origin airport code they provided is not valid
    # I use f-string formatting to include the user-input origin airport code in the error message
    # I also exit the program with a non-zero status code to indicate an error using exit(1) which is a common practice in command-line applications
    # This indicates that the program encountered an error and did not complete successfully
    print(f"❌ Error: Origin airport code '{args.origin}' not found in the route data.")
    exit(1)
# This if statement checks if the destination airport code provided by the user is in the all_airports set
# If the destination airport code is not found, it prints an error message and exits the program
# This message will inform the user that the destination airport code they provided is not valid (same as above)
if args.destination not in all_airports:
    # Then again, I am printing an error message if the destination airport code is not found in the all_airports set
    print(f"❌ Error: Destination airport code '{args.destination}' not found in the route data.")
    exit(1)

# This if statement is optional and is used for debugging purposes
if args.debug:
    # If the user provides the --debug flag when running the script, it will print the loaded routes
    print("\n🔧 DEBUG: Loaded Routes:")
    # this for loop iterates throught the graph's routes dictionary
    # For each origin airport, it prints the destination airports and their respective distances
    # This is useful for verifying that the routes were loaded correctly from the CSV file
    for origin, destinations in graph.routes.items():
        for dest, dist in destinations.items():
            print(f"  {origin} -> {dest} ({dist} miles)")

# I use this print statement to inform the user about the search
print(f"\n🧭 Searching route from 🛫 {args.origin} to 🛬{args.destination}...\n")

# This line calls the shortest_path method on the graph instance to find the shortest route from the origin to the destination
# The method returns the cost (distance) and the path taken
# The cost is the total distance of the shortest route, and the path is a list of airport codes representing the route taken
# This method uses Dijkstra's algorithm to find the shortest path in the graph
cost, path = graph.shortest_path(args.origin, args.destination)

# This if statement checks if the cost is infinite, meaning no route was found
# If the cost is infinite, it means that there is no valid route between the origin and destination airports
if cost == float("inf"):
    # In this case, I'm printing a message indicating that no route was found
    # This message will inform the user that there is no valid route between the specified airports
    print("🚫 No route found between the specified airports.")
else:
    # If a route was found, i'm printing the shortest route and its cost
    print("\n✅ Shortest Route Found:")
    # .join(path) is used to join the list of airport codes into a single string, seperated by " → "
    print(f"  🛫  Route: {' → '.join(path)}")
    # this line prints the total distance of the route
    print(f"  📏  Total Distance: {cost} miles")


