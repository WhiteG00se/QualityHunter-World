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
        # entry["Defense (ushort)"] = math.ceil(entry["Defense (ushort)"] * 1.75)
        entry["Fire Res (byte)"] = max(0, entry["Fire Res (byte)"])
        entry["Water Res (byte)"] = max(0, entry["Water Res (byte)"])
        entry["Ice Res (byte)"] = max(0, entry["Ice Res (byte)"])
        entry["Thunder Res (byte)"] = max(0, entry["Thunder Res (byte)"])
        entry["Dragon Res (byte)"] = max(0, entry["Dragon Res (byte)"])
        if entry["Equip Slot (ubyte)"] == 5 and entry["Skill 1 (ushort)"] != 0:
            if entry["Skill 1 (ushort)"] != 104: # 104: Flinch Free
                if entry["Skill 2 (ushort)"] == 0:
                    entry["Skill 2 (ushort)"] = 104
                    entry["Skill 2 Level (ubyte)"] = 1
                else:
                    entry["Skill 3 (ushort)"] = 104
                    entry["Skill 3 Level (ubyte)"] = 1
            else:
                entry["Skill 2 (ushort)"] = 97  # 97: Divine Blessing
                entry["Skill 2 Level (ubyte)"] = 1
        if entry["Defense (ushort)"] >= 1:
            if entry["Skill 1 (ushort)"] == 23: # 23: Recovery Speed
                entry["Skill 1 (ushort)"] = 22 # 22: Recovery Up
            elif entry["Skill 2 (ushort)"] == 23:
                entry["Skill 2 (ushort)"] = 22
            elif entry["Skill 3 (ushort)"] == 23:
                entry["Skill 3 (ushort)"] = 22
                

data = parse_json_file(inputFile)
modify_entry(data)
write_json_file(data, outputFile)
