import json
import struct
import requests

file_path = "src/armor.am_dat"
file_type = file_path.split(".")[-1]

def parse_template(url):
    # Send an HTTP GET request to the URL
    datatypes = '<'
    dict_datatypes = {" uint": "I", " int": "i", " ubyte": "B", " byte": "b", " ushort": "H", " ushort": "h"}
    response = requests.get(url)
    lines = response.text.split('\n')
    for line in lines:
        for el in dict_datatypes.keys():
            if el in line:
                datatypes += dict_datatypes[el]
    return datatypes

# Define the structure formats
header_format = '<IHI'
entry_format = '<IhBhBBhhhhBBIbbbbbBBBBhBhBhBhBhBIhhhB'

github_template_url = f"https://raw.githubusercontent.com/Synthlight/MHW-Editor/master/010%20Templates/{file_type}.bt"
print(parse_template(github_template_url))

# Define the structure sizes
header_size = struct.calcsize(header_format)
entry_size = struct.calcsize(entry_format)


# Function to read the header
def read_header(file):
    header_data = file.read(header_size)
    return struct.unpack(header_format, header_data)


# Function to read an entry
def read_entry(file):
    entry_data = file.read(entry_size)
    return struct.unpack(entry_format, entry_data)


# Open the binary file
with open(file_path, 'rb') as file:
    # Read the header
    header = read_header(file)
    print("Header:")
    print("Magic 1 (uint):", header[0])
    print("Magic 2 (ushort):", header[1])
    print("Entry Count (uint):", header[2])

    # Read entries
    print("\nEntries:")
    for i in range(header[2]):
        entry = read_entry(file)
        print("\nEntry", i + 1)
        print("Index (uint):", entry[0])
        print("Order (ubyte):", entry[1])
        print("Variant (ubyte):", entry[2])
        print("Set (Layered) Id (ushort):", entry[3])
        print("Type (ubyte):", entry[4])
        print("Equip Slot (ubyte):", entry[5])
        print("Defense (ushort):", entry[6])
        print("Model Id 1 (ushort):", entry[7])
        print("Model Id 2 (ushort):", entry[8])
        print("Icon Color (ushort):", entry[9])
        print("Icon Effect (ubyte):", entry[10])
        print("Rarity (ubyte):", entry[11])
        print("Cost (uint):", entry[12])
        print("Fire Res (ubyte):", entry[13])
        print("Water Res (ubyte):", entry[14])
        print("Ice Res (ubyte):", entry[15])
        print("Thunder Res (ubyte):", entry[16])
        print("Dragon Res (ubyte):", entry[17])
        print("Slot Count (ubyte):", entry[18])
        print("Slot 1 Size (ubyte):", entry[19])
        print("Slot 2 Size (ubyte):", entry[20])
        print("Slot 3 Size (ubyte):", entry[21])
        print("Set Skill 1 (ushort):", entry[22])
        print("Set Skill 1 Level (ubyte):", entry[23])
        print("Hidden Skill (ushort):", entry[24])
        print("Hidden Skill Level (ubyte):", entry[25])
        print("Skill 1 (ushort):", entry[26])
        print("Skill 1 Level (ubyte):", entry[27])
        print("Skill 2 (ushort):", entry[28])
        print("Skill 2 Level (ubyte):", entry[29])
        print("Skill 3 (ushort):", entry[30])
        print("Skill 3 Level (ubyte):", entry[31])
        print("Gender (uint):", entry[32])
        print("Set Group (ushort):", entry[33])
        print("GMD Name Index (ushort):", entry[34])
        print("GMD Description Index (ushort):", entry[35])
        print("Is Permanent (ubyte):", entry[36])
