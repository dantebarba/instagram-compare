import json
import sys

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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py source_file.json compare_file.json")
    else:
        source_file = sys.argv[1]
        compare_file = sys.argv[2]
        
        result = compare_json(source_file, compare_file)
        
        # Print the result as formatted JSON
        print(json.dumps(result, indent=4))
