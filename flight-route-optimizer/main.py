# I am importing the argparse module, which allows me to handle command-line arguments in a clean and user-friendly way
import argparse 

# Creating an ArgumentParser object that will hold the logic for parsing command-line arguments
# The 'description' parameter provides a helpful summary that will show up when the user runs the script with --help
parser = argparse.ArgumentParser(description="Find shortest flight route between two airports.")

# Defining the first positional argument: 'origin'
# This means the user must supply an airport code (e.g., BWI) as the first argument
# type=str ensures the input is treated as a string
# help gives a short explanation that will show when the user asks for help
parser.add_argument("origin", type=str, help=" airport code (e.g., BWI)")

# Defining the second positional argument: 'destination'
# This argument will come second in the command-line input
# Also enforced as a string, and help gives an example for clarity
parser.add_argument("destination", type=str, help="Destination airport code(e.g., HOU)")

# Parsing the arguments passed by the user and store them in the 'args' variable
# For example, if the user runs `python main.py BWI HOU`, then:
# args.origin = "BWI" and args.destination = "HOU"
args = parser.parse_args()


# Output the origin and destination provided by the user, using f-string formatting
# This is helpful for confirming that the inputs were received and understood correctly
print(f"Searching route from {args.origin} to {args.destination}")