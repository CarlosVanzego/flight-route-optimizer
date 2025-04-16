import argparse
from graph import Graph

# Create the CLI parser
parser = argparse.ArgumentParser(description="Find shortest flight route between two airports.")
parser.add_argument("origin", type=str, help="Origin airport code (e.g., BWI)")
parser.add_argument("destination", type=str, help="Destination airport code (e.g., HOU)")
parser.add_argument("--debug", action="store_true", help="Show route graph data for debugging")

# Parse command-line arguments
args = parser.parse_args()

# Initialize graph and load routes
graph = Graph()
graph.load_from_csv("routes.csv")

# Create a combined list of all valid airport codes
all_airports = set(graph.routes.keys())
for neighbors in graph.routes.values():
    all_airports.update(neighbors.keys())

# Validate origin and destination
if args.origin not in all_airports:
    print(f"❌ Error: Origin airport code '{args.origin}' not found in the route data.")
    exit(1)

if args.destination not in all_airports:
    print(f"❌ Error: Destination airport code '{args.destination}' not found in the route data.")
    exit(1)

# Optional debugging output
if args.debug:
    print("\n🔧 DEBUG: Loaded Routes:")
    for origin, destinations in graph.routes.items():
        for dest, dist in destinations.items():
            print(f"  {origin} -> {dest} ({dist} miles)")

# Inform the user about the search
print(f"\n🧭 Searching route from 🛫 {args.origin} to 🛬{args.destination}...\n")

# Run shortest path search
cost, path = graph.shortest_path(args.origin, args.destination)

# Display the result
if cost == float("inf"):
    print("🚫 No route found between the specified airports.")
else:
    print("\n✅ Shortest Route Found:")
    print(f"  🛫  Route: {' → '.join(path)}")
    print(f"  📏  Total Distance: {cost} miles")





















# # I am importing the argparse module, which allows me to handle command-line arguments in a clean and user-friendly way
# import argparse 
# # Importing the Graph class from the graph module
# from graph import Graph

# # Creating an ArgumentParser object that will hold the logic for parsing command-line arguments
# # The 'description' parameter provides a helpful summary that will show up when the user runs the script with --help
# parser = argparse.ArgumentParser(description="Find shortest flight route between two airports.")

# # Defining the first positional argument: 'origin'
# # This means the user must supply an airport code (e.g., BWI) as the first argument
# # type=str ensures the input is treated as a string
# # help gives a short explanation that will show when the user asks for help
# parser.add_argument("origin", type=str, help=" airport code (e.g., BWI)")

# # Defining the second positional argument: 'destination'
# # This argument will come second in the command-line input
# # Also enforced as a string, and help gives an example for clarity
# parser.add_argument("destination", type=str, help="Destination airport code(e.g., HOU)")

# # This optional argument allows the user to specify a different CSV file for the routes
# # The default value is set to "routes.csv", so if the user doesn't provide this argument, it will use that file
# # type=str, ensures the input is treated as a string
# # help provides a short explanation that will show when the user asks for help
# parser.add_argument("--file", type=str, default="routes.csv", help="Path to route CSV file (default: routes.csv)")

# # Parsing the arguments passed by the user and store them in the 'args' variable
# # For example, if the user runs `python main.py BWI HOU`, then:
# # args.origin = "BWI" and args.destination = "HOU"
# args = parser.parse_args()


# # Output the origin and destination provided by the user, using f-string formatting
# # This is helpful for confirming that the inputs were received and understood correctly
# print(f"Searching route from {args.origin} to {args.destination}")

# # Creating an instance of the Graph class
# graph = Graph()
# # Loading the routes from a CSV file into the graph instance
# graph.load_from_csv(args.file)

# # this if statement validates that the user-input airports actually exist in the data
# if args.origin not in graph.routes:
#   print(f"❌ Error: Origin airport code '{args.origin}' not found in the route data.")
#   exit(1)

# # this line creates a set of all destination airports from the graphs routes
# all_destinations = {dest for dests in graph.routes.values() for dest in dests}
# if args.destination not in all_destinations:
#   print(f"❌ Destination airport code '{args.destination}' not found in the route data.")
#   exit(1) 

# # Calling the shortest_path method on the graph instance to find the shortest route from the origin to the destination
# cost, path = graph.shortest_path(args.origin, args.destination)

# # If statement to check if the cost is infinite, meaning no route was found
# if cost == float("inf"):
#   # Printing a message indicating that no route was found
#   print("No route found")
# # If a route was found, this will print the shortest route and its cost. 
# else:
#   print("\n✅ Shortest Route Found:")
#   print(f"🛫 Route: {' -> '.join(path)}")
#   print(f"📏 Total Distance: {cost} miles")