import configparser
import pathlib
import json
import os

# Initialize the parser

def readconfigfile():
    config = configparser.ConfigParser()

    # Read the file
    config_path = pathlib.Path(__file__).parent.parent / 'configs' / 'config.ini'
    config.read(config_path)

    # Access values like a nested dictionary
    base_url = config['url']['base_url']
    return base_url





