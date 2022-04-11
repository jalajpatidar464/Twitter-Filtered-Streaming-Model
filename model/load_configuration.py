import json


def load_configuration_file():
    """Returning data of JSON file containing configurations"""
    with open("configuration.json", 'r') as fil:
        data = json.load(fil)
    return data
