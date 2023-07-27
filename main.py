import json
import argparse

def compare_json(source, compare):
    # Load JSON data from files
    with open(source, 'r') as f:
        source_data = json.load(f)
    with open(compare, 'r') as f:
        compare_data = json.load(f)
    
    # Create a dictionary for faster lookup based on username
    source_dict = {entry['username']: entry for entry in source_data}
    
    # Filter out elements from compare_data that are not in source_data
    result_data = [entry for entry in compare_data if entry['username'] not in source_dict]
    
    return result_data

def main():
    parser = argparse.ArgumentParser(description="Compare two JSON files based on the 'username' key.")
    parser.add_argument("source", help="Path to the source JSON file.")
    parser.add_argument("compare", help="Path to the compare JSON file.")
    args = parser.parse_args()

    result = compare_json(args.source, args.compare)

    # Print the result as formatted JSON
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
