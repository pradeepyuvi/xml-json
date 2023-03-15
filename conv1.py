import xmltodict
import json
import time

# read the XML file
with open('input.xml', 'r') as file:
    xml_data = file.read()

# convert XML to JSON and measure the time taken
start_time = time.time()
json_data = json.dumps(xmltodict.parse(xml_data), indent=4)
end_time = time.time()

# print the JSON output and time taken
# print(json_data)
print(f"\nTime taken for conversion: {end_time - start_time} seconds")

with open("data1.json", "w") as json_file:
		json_file.write(json_data)
