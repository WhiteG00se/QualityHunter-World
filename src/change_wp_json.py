from pathlib import Path
import json

input_folder = Path("src/vanilla_files")
output_folder = Path("src/changed_files")

def parse_json_file(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
        return data

def write_json_file(data, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def modify_entry(data):
    for entry in data["Entries"]:
        entry["Defense (ushort)"] *= 3

for file in input_folder.iterdir():
    if file.suffix != ".json":
        continue
    if Path(file.stem).suffix != ".wp_dat" and Path(file.stem).suffix != ".wp_dat_g":
        continue
    data = parse_json_file(file)
    modify_entry(data)
    write_json_file(data, output_folder / file.name)