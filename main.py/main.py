import argparse

parser = argparse.ArgumentParser(description="Find shortest flight route between two airports.")
parser.add_Argument("origin", type=str, help="Origin airport code (e.g. BWI)")
parser.add_argument("destination", type=str, help="Destination airport code (e.g., LAX)")
args = parser.parse_args()

print(f"Searching route from {args.origin} to {args.destination}")

