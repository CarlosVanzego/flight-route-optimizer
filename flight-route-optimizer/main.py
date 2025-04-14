import argparse 

# Create the CLI (Command Line Interface) parser
parser = argparse.ArgumentParser(description="Find shortest flight route between two airports.")
parser.add_argument("origin", type=str, help=" airport code (e.g., BWI)")
parser.add_argument("destination", type=str, help="Destination airport code(e.g., HOU)")
args = parser.parse_args()

print(f"Searching route from {args.origin} to {args.destination}")