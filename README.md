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

# Ensure the request was successful
if response.status_code == 200:
    # Parse the JSON incrementally using ijson
    parser = ijson.parse(response.raw)
    
    current_field = None
    
    for prefix, event, value in parser:
        if (prefix, event) == ('columns.item.name', 'string'):
            # Collect column names
            columns.append({'name': value})
            current_field = 'name'
        
        elif (prefix, event) == ('columns.item.type', 'string') and current_field == 'name':
            # Add type to the last added column
            columns[-1]['type'] = value
            current_field = None
            
        elif prefix.startswith('rows.item.values.item'):
            # Collect row values
            if 'values' not in rows:
                rows.append({'values': []})
            rows[-1]['values'].append(value)
    
    # At this point, columns and rows should be fully populated
    print("Columns:", columns)
    for row in rows:
        print("Row:", row['values'])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
