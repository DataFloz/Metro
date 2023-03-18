import yaml
from models.transformation_cfg import TransformationConfig

CONFIGURATION_FILE = './cfg/metro.yaml'

def read_configuration_file():
    # opening a file
    with open(CONFIGURATION_FILE, 'r') as stream:
        try:
            # Converts yaml document to python object
            d=yaml.safe_load(stream)
            return d
            # Printing dictionary
            # print(d)
        except yaml.YAMLError as e:
            print(e)
