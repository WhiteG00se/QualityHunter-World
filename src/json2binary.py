from pathlib import Path
import json
import struct

file_path = "armor.am_dat.json"
file_out = "src/armor_converted.am_dat"

file_type = Path(file_path).stem.split(".")[-1]

# Define the structure formats
header_format = '<IHI'
entry_format = '<IhBhBBhhhhBBIbbbbbBBBBhBhBhBhBhBIhhhB'

# Function to write the header to the binary file
def write_header(file, data_header):
    file.write(struct.pack(header_format, *data_header.values()))

# Function to write an entry to the binary file
def write_entry(file, entry):
    file.write(struct.pack(entry_format, *entry.values()))

# Read JSON data from file
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

# Open binary file for writing
with open(file_out, 'wb') as binary_file:
    # Write header
    write_header(binary_file, data["Header"])

    # Write entries
    for entry in data['Entries']:
        write_entry(binary_file, entry)

print("Binary file created successfully.")
