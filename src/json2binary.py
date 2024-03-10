from pathlib import Path
import json
import struct
from utils import parse_template

file_in = "src\changed_files\common-equip-armor.am_dat.json"
file_out = Path(file_in).stem

file_type = Path(file_in).stem.split(".")[-1]

# Define the structure formats
github_template_url = f"https://raw.githubusercontent.com/Synthlight/MHW-Editor/master/010%20Templates/{file_type}.bt"
datatypes, datanames = parse_template(github_template_url)

# Function to write the header to the binary file
def write_header(file, data_header):
    file.write(struct.pack(datatypes["Header"], *data_header.values()))

# Function to write an entry to the binary file
def write_entry(file, entry):
    file.write(struct.pack(datatypes["Entries"], *entry.values()))

# Read JSON data from file
with open(file_in, 'r') as json_file:
    data = json.load(json_file)

# Open binary file for writing
with open(file_out, 'wb') as binary_file:
    # Write header
    write_header(binary_file, data["Header"])

    # Write entries
    for entry in data['Entries']:
        write_entry(binary_file, entry)
