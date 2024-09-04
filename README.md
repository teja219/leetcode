# leetcode
Collection of LeetCode questions to ace the coding interview! - Created using [LeetHub](https://github.com/QasimWani/LeetHub)
import requests
import ijson

# Example URL, replace with your actual data source
url = "https://example.com/large-data-stream"

# Make a streaming GET request
response = requests.get(url, stream=True)

# Initialize empty lists to hold columns and rows
columns = []
rows = []

if response.status_code == 200:
    # Parse the JSON incrementally using ijson
    parser = ijson.parse(response.raw)
    
    current_row = None
    
    for prefix, event, value in parser:
        if prefix == 'columns.item.name':
            columns.append({'name': value})
        elif prefix == 'columns.item.type':
            columns[-1]['type'] = value
        elif prefix == 'rows.item.values.item':
            # Check if we are processing a new row
            if current_row is None:
                current_row = []
            current_row.append(value)
        elif prefix == 'rows.item.values' and event == 'end_array':
            # End of the current row, add it to rows list
            rows.append(current_row)
            current_row = None
    
    # At this point, columns and rows should be fully populated
    print("Columns:", columns)
    for row in rows:
        print("Row:", row)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

