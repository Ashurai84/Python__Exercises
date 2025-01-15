# 107 Write a script that reads a JSON file, modifies a value, and writes the updated data back to the file
import json

def modify_json(file_path, key, new_value):
    with open(file_path, 'r') as file:
        data = json.load(file)

    data[key] = new_value

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
file_path = "data.json"
modify_json(file_path, "name", "New Name")