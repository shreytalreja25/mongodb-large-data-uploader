import xmltodict
import json

# Define the file path for the XML input file
xml_file_path = r'C:\Users\Piyush Ratta\Desktop\New folder\formy.xml'

# Read XML data
with open(xml_file_path, 'r') as xml_file:
    xml_data = xml_file.read()

# Convert XML to JSON
json_data = json.dumps(xmltodict.parse(xml_data), indent=4)

# Define the file path for the JSON output file
json_file_path = r'C:\Users\Piyush Ratta\Desktop\New folder\data.json'

# Write JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)
