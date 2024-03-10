import json
import math

inputFile = 'src\\vanilla_files\\common-equip-armor.am_dat.json'
outputFile = 'src\\common-equip-armor.am_dat.json'

def parse_json_file(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
        return data

def write_json_file(data, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def modify_entry(data):
    for entry in data["Entries"]:
        entry["Defense (ushort)"] = math.ceil(entry["Defense (ushort)"] * 2)
        entry["Fire Res (byte)"] = max(0, entry["Fire Res (byte)"])
        entry["Water Res (byte)"] = max(0, entry["Water Res (byte)"])
        entry["Ice Res (byte)"] = max(0, entry["Ice Res (byte)"])
        entry["Thunder Res (byte)"] = max(0, entry["Thunder Res (byte)"])
        entry["Dragon Res (byte)"] = max(0, entry["Dragon Res (byte)"])

data = parse_json_file(inputFile)
modify_entry(data)
write_json_file(data, outputFile)
