import requests

def parse_template(url):
    # Send an HTTP GET request to the URL
    datanames = {}
    datatypes = {}
    dict_datatypes = {
        " uint": "I",
        " int": "i",
        " ubyte": "B",
        " byte": "b",
        " ushort": "H",
        " ushort": "h"
    }
    response = requests.get(url)
    structs = response.text.split("struct")
    for text_struct in structs[1:]:
        struct_type = text_struct[(text_struct.rfind('}')):].split(';')[0]
        struct_type = struct_type.strip("}").strip(" ")
        lines = text_struct.split('\n')
        datanames_struct = []
        datatypes_struct = '<'
        for line in lines:
            for el in dict_datatypes.keys():
                if el in line:
                    datatypes_struct += dict_datatypes[el]
                    name = line[line.rfind('name="'):].split('"')[1]
                    datanames_struct.append(name)
        datanames[struct_type] = datanames_struct
        datatypes[struct_type] = datatypes_struct
    return datatypes, datanames
