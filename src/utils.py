import requests

def parse_template(url):
    # Send an HTTP GET request to the URL
    datanames = []
    datatypes = '<'
    dict_datatypes = {" uint": "I", " int": "i", " ubyte": "B", " byte": "b", " ushort": "H", " ushort": "h"}
    response = requests.get(url)
    lines = response.text.split('\n')
    for line in lines:
        for el in dict_datatypes.keys():
            if el in line:
                datatypes += dict_datatypes[el]
                name = line[line.rfind('name="'):].split('"')[1]
                datanames.append(name)
    return datatypes, datanames
